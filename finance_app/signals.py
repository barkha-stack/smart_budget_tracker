from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
from datetime import date

from .models import Expense, Budget
from .tasks import send_budget_alert_task


@receiver(post_save, sender=Expense)
def check_budget_and_alert(sender, instance, created, **kwargs):
    """
    Automatically checks budget usage after every expense
    and triggers alert if usage >= 80%
    """

    # Only trigger when a NEW expense is created
    if not created:
        return

    user = instance.user
    category = instance.category

    if not category:
        return

    today = date.today()

    # Get user's budget for this category/month
    try:
        budget = Budget.objects.get(
            user=user,
            category=category,
            month=today.month,
            year=today.year
        )
    except Budget.DoesNotExist:
        return  # No budget set → no alert

    # Total spent in this category this month
    spent = (
        Expense.objects.filter(
            user=user,
            category=category,
            date__month=today.month,
            date__year=today.year
        ).aggregate(total=Sum("amount"))["total"] or 0
    )

    percent_used = int((spent / budget.monthly_limit) * 100)

    # Trigger alert if crossed 80%
    if percent_used >= 80:
        send_budget_alert_task.delay(
            user_id=user.id,
            category=category.name,
            percent_used=percent_used,
            phone=None,          # add later
            email=user.email
        )
