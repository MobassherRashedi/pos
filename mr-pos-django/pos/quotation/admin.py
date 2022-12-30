from django.contrib import admin

from .models import QuotationCart, QuotationCartAmount, Quotation


@admin.register(QuotationCart)
class QuotationCartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'user',
        'product',
        'quantity',
        'sales_rate',
        'total_amount',
    )
    list_filter = ('created_at', 'updated_at', 'user', 'product')
    date_hierarchy = 'created_at'


@admin.register(QuotationCartAmount)
class QuotationCartAmountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'cart',
        'sub_total',
        'vat',
        'vat_amount',
        'discount',
        'discount_amount',
        'total',
    )
    list_filter = ('created_at', 'updated_at', 'cart')
    date_hierarchy = 'created_at'


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'invoice_no',
        'purchased_by',
        'customer_name',
        'phone',
        'address',
        'product',
        'sales_rate',
        'qty',
        'stock',
        'totla_for_specific_item',
        'returened',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'purchased_by',
        'product',
        'returened',
    )
    date_hierarchy = 'created_at'