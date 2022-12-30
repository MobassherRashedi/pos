from django.contrib import admin

from .models import User, UserProfile, CustomerTransaction, SupplierTransaction


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'last_login',
        'is_superuser',
        'username',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'date_joined',
        'phone_number',
        'password',
        'address',
        'phone_1',
        'phone_2',
        'email',
        'status',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'status',
    )
    raw_id_fields = ('groups', 'user_permissions')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'user',
        'date_of_birth',
        'gender',
        'profile_picture',
        'status',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'user',
        'date_of_birth',
        'status',
    )
    date_hierarchy = 'created_at'


@admin.register(CustomerTransaction)
class CustomerTransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'transaction_date',
        'customer',
        'customer_name',
        'due',
        'transaction_id',
        'transaction_type',
        'amount',
        'note',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'transaction_date',
        'customer',
        'transaction_type',
    )
    date_hierarchy = 'created_at'


@admin.register(SupplierTransaction)
class SupplierTransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'transaction_date',
        'supplier',
        'supplier_name',
        'due',
        'transaction_id',
        'transaction_type',
        'amount',
        'note',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'transaction_date',
        'supplier',
        'transaction_type',
    )
    date_hierarchy = 'created_at'
