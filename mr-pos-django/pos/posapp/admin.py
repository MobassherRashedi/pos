from django.contrib import admin

from .models import Category, Products, Sales, salesItems


@admin.register(Category)
class PosCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'status',
        'date_added',
        'date_updated',
    )
    list_filter = ('date_added', 'date_updated')
    search_fields = ('name',)


@admin.register(Products)
class PosProductsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'code',
        'category_id',
        'name',
        'description',
        'price',
        'status',
        'date_added',
        'date_updated',
    )
    list_filter = ('category_id', 'date_added', 'date_updated')
    search_fields = ('name',)


@admin.register(Sales)
class PosSalesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'code',
        'sub_total',
        'grand_total',
        'tax_amount',
        'tax',
        'tendered_amount',
        'amount_change',
        'date_added',
        'date_updated',
    )
    list_filter = ('date_added', 'date_updated')


# @admin.register(salesItems)
# class PossalesItemsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'sale_id', 'product_id', 'price', 'qty', 'total')
#     list_filter = ('sale_id', 'product_id')