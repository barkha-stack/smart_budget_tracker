from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Income, Expense
from .forms import IncomeForm, ExpenseForm

# -----------------------------
# DASHBOARD VIEW
# -----------------------------
@login_required
def dashboard(request):
    # Handle income form submission
    if request.method == 'POST' and 'income_submit' in request.POST:
        income_form = IncomeForm(request.POST)
        if income_form.is_valid():
            income = income_form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('dashboard')

    # Handle expense form submission
    elif request.method == 'POST' and 'expense_submit' in request.POST:
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense = expense_form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('dashboard')

    else:
        income_form = IncomeForm()
        expense_form = ExpenseForm()

    # Fetch user data
    incomes = Income.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)

    total_income = sum(i.amount for i in incomes)
    total_expense = sum(e.amount for e in expenses)
    balance = total_income - total_expense

    context = {
        'income_form': income_form,
        'expense_form': expense_form,
        'incomes': incomes,
        'expenses': expenses,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }

    return render(request, 'finance_app/dashboard.html', context)
