from django.db import models
from django.contrib.auth.models import User

# -----------------------------
# CATEGORY choices (fixed list)
# -----------------------------
CATEGORY_CHOICES = [
    ('Food', 'Food'),
    ('Rent', 'Rent'),
    ('Travel', 'Travel'),
    ('Shopping', 'Shopping'),
    ('Bills', 'Bills'),
    ('Other', 'Other'),
]

# -----------------------------
# INCOME MODEL
# -----------------------------
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"


# -----------------------------
# EXPENSE MODEL
# -----------------------------
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.amount}"
