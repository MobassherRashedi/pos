from django.contrib import admin

from .models import Catagory, SubCatagory, Customer, Supplier, CompanyInfo


@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'name', 'status')
    list_filter = ('created_at', 'updated_at', 'status')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(SubCatagory)
class SubCatagoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'name',
        'catagory',
        'status',
    )
    list_filter = ('created_at', 'updated_at', 'catagory', 'status')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'first_name',
        'last_name',
        'customer_code',
        'address',
        'phone_1',
        'phone_2',
        'email',
        'previous_due',
    )
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'first_name',
        'last_name',
        'supplier_code',
        'address',
        'phone_1',
        'phone_2',
        'email',
        'previous_due',
    )
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'name',
        'moto',
        'address',
        'phone_1',
        'phone_2',
        'bin',
        'logo',
        'email',
        'invoice_print_type',
    )
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'