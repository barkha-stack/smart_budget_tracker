from django.db import models
from django.contrib.auth.models import User


# =====================================================
# CATEGORY MODEL
# =====================================================
class Category(models.Model):
    """
    Stores expense categories for a specific user.
    Example:
    Food, Travel, Shopping, Rent, Medical, etc.
    """

    # Category name (e.g., Food, Travel)
    name = models.CharField(max_length=100)

    # Each user has their own categories
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="categories"
    )

    class Meta:
        # Prevents duplicate category names per user
        unique_together = ("user", "name")
        ordering = ["name"]

    def __str__(self):
        return self.name


# =====================================================
# INCOME MODEL
# =====================================================
class Income(models.Model):
    """
    Stores user's income sources such as:
    Salary, Pocket Money, Freelance, Business, etc.
    """

    # Owner of the income record
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="incomes"
    )

    # Source of income
    source = models.CharField(max_length=100)

    # Amount earned (DecimalField is mandatory for money)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Date when income was received
    # (Editable in case user wants to add past income)
    date = models.DateField()

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.source} - ₹{self.amount}"


# =====================================================
# EXPENSE MODEL
# =================================================from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Expense(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="expenses"
    )

    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # ✅ SAFE DEFAULT (prevents NULL errors forever)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - ₹{self.amount}"

# =====================================================
# BUDGET MODEL
# =====================================================
class Budget(models.Model):
    """
    Stores monthly budget per category.
    Used for:
    - Percentage calculations
    - Overspending alerts
    - Email / SMS / WhatsApp notifications
    """

    # Budget owner
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="budgets"
    )

    # Category this budget applies to
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    # Monthly spending limit
    monthly_limit = models.DecimalField(max_digits=10, decimal_places=2)

    # Month & Year allow tracking budgets historically
    month = models.IntegerField(help_text="1 = January, 12 = December")
    year = models.IntegerField()

    class Meta:
        # Prevents duplicate budgets for same category & month
        unique_together = ("user", "category", "month", "year")
        ordering = ["-year", "-month"]

    def __str__(self):
        return f"{self.category.name} | ₹{self.monthly_limit} ({self.month}/{self.year})"
