from django import forms
from .models import Income, Expense

# -----------------------------
# INCOME FORM
# -----------------------------
class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'source']

        # Add Bootstrap styling
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'source': forms.TextInput(attrs={'class': 'form-control'}),
        }


# -----------------------------
# EXPENSE FORM
# -----------------------------
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
