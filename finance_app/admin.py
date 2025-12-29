from django.contrib import admin
from .models import Category, Income, Expense, Budget


# ----------------------------
# CATEGORY ADMIN
# ----------------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "user")
    search_fields = ("name",)


# ----------------------------
# INCOME ADMIN
# ----------------------------
@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ("source", "amount", "user", "date")
    list_filter = ("date",)
    search_fields = ("source",)


# ----------------------------
# EXPENSE ADMIN
# ----------------------------
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("title", "amount", "category", "user", "date")
    list_filter = ("category", "date")
    search_fields = ("title",)


# ----------------------------
# BUDGET ADMIN
# ----------------------------
@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ("category", "monthly_limit", "month", "year", "user")
    list_filter = ("month", "year", "category")
