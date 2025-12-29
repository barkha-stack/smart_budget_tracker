from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import date

from .models import Income, Expense, Budget


@login_required
def dashboard(request):
    user = request.user
    today = date.today()

    total_income = (
        Income.objects.filter(user=user)
        .aggregate(total=Sum("amount"))["total"] or 0
    )

    total_expense = (
        Expense.objects.filter(user=user)
        .aggregate(total=Sum("amount"))["total"] or 0
    )

    balance = total_income - total_expense

    budgets = Budget.objects.filter(
        user=user,
        month=today.month,
        year=today.year
    )

    budget_status = []

    for budget in budgets:
        spent = (
            Expense.objects.filter(
                user=user,
                category=budget.category,
                date__month=today.month,
                date__year=today.year
            ).aggregate(total=Sum("amount"))["total"] or 0
        )

        percent = int((spent / budget.monthly_limit) * 100)

        # 🎨 Color logic
        if percent >= 80:
            color = "danger"
        elif percent >= 50:
            color = "warning"
        else:
            color = "success"

        budget_status.append({
            "category": budget.category.name,
            "limit": budget.monthly_limit,
            "spent": spent,
            "percent": percent,
            "color": color
        })

    context = {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "budget_status": budget_status,
    }

    return render(request, "finance_app/dashboard.html", context)
