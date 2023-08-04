from django.contrib import admin
from .models import Expense

# Expense model register in django admin panel
@admin.register(Expense)
class ExpenseModel(admin.ModelAdmin):
    list_display = ('exp_title', 'exp_user', 'exp_description', 'exp_date')