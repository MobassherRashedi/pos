from django.contrib import admin

from .models import Bank, BankTransactionType, BankTransaction


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'name',
        'account_name',
        'account_number',
        'branch',
        'initial_balance',
    )
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(BankTransactionType)
class BankTransactionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'name')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(BankTransaction)
class BankTransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'bank_account',
        'bank_transaction_type',
        'branch',
        'amount',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'bank_account',
        'bank_transaction_type',
    )
    date_hierarchy = 'created_at'