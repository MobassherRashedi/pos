from django.contrib import admin

from .models import SalesCart, SalesCartAmount, Sales


admin.site.register(SalesCart)
admin.site.register(SalesCartAmount)
admin.site.register(Sales)

# @admin.register(SalesCart)
# class SalesCartAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'created_at',
#         'updated_at',
#         'user',
#         'product',
#         'quantity',
#         'sales_rate',
#         'total_amount',
#     )
#     list_filter = ('created_at', 'updated_at', 'user', 'product')
#     date_hierarchy = 'created_at'


# @admin.register(SalesCartAmount)
# class SalesCartAmountAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'created_at',
#         'updated_at',
#         'cart',
#         'sub_total',
#         'vat',
#         'vat_amount',
#         'discount',
#         'discount_amount',
#         'Transport',
#         'total',
#         'paid',
#         'due',
#     )
#     list_filter = ('created_at', 'updated_at', 'cart')
#     date_hierarchy = 'created_at'


# @admin.register(Sales)
# class SalesAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'created_at',
#         'updated_at',
#         'invoice_no',
#         'purchased_by',
#         'barcode',
#         'customer',
#         'phone',
#         'address',
#         'product',
#         'sales_rate',
#         'qty',
#         'stock',
#         'totla_for_specific_item',
#         'returened',
#     )
#     list_filter = (
#         'created_at',
#         'updated_at',
#         'purchased_by',
#         'customer',
#         'product',
#         'returened',
#     )
#     date_hierarchy = 'created_at'