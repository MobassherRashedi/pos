from django.contrib import admin
from .models import Expenses,ExpensesCatagory,ExpensesSubCatagory


admin.site.register(Expenses)
admin.site.register(ExpensesCatagory)
admin.site.register(ExpensesSubCatagory)
