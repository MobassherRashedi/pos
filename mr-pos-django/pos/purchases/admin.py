from django.contrib import admin

from .models import PurchaseCart, PurchaseCartAmount, Purchase


@admin.register(PurchaseCart)
class PurchaseCartAdmin(admin.ModelAdmin):
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


@admin.register(PurchaseCartAmount)
class PurchaseCartAmountAdmin(admin.ModelAdmin):
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
        'Transport',
        'total',
        'paid',
        'due',
    )
    list_filter = ('created_at', 'updated_at', 'cart')
    date_hierarchy = 'created_at'


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'invoice_no',
        'purchased_by',
        'catagory',
        'sub_catagory',
        'supplier',
        'product',
        'purchase_rate',
        'qty',
        'sales_rate',
        'stock',
        'totla_for_specific_item',
        'selling_price',
        'returened',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'purchased_by',
        'catagory',
        'sub_catagory',
        'supplier',
        'product',
        'returened',
    )
    date_hierarchy = 'created_at'