from celery import shared_task
from django.contrib.auth.models import User
from .utils.alerts import send_budget_email


@shared_task
def send_budget_alert_task(user_id, category, percent_used, phone, email):
    """
    Background task for budget alerts
    """

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return

    if email:
        send_budget_email(
            user=user,
            category=category,
            spent_percent=percent_used
        )
