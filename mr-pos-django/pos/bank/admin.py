from django.contrib import admin

from .models import Bank,BankTransaction,BankTransactionType

admin.site.register(Bank)
admin.site.register(BankTransaction)
admin.site.register(BankTransactionType)