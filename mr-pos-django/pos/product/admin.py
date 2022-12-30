from django.contrib import admin

from .models import ProductImages, ProductUnitType, Product


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'file', 'status')
    list_filter = ('created_at', 'updated_at', 'status')
    date_hierarchy = 'created_at'


@admin.register(ProductUnitType)
class ProductUnitTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'name',
        'description',
        'status',
    )
    list_filter = ('created_at', 'updated_at', 'status')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'name',
        'slug',
        'product_code',
        'catagory',
        'sub_catagory',
        'product_unit',
        'alert_qty',
        'purchase_rate',
        'sales_rate',
        'status',
        'returned',
        'damaged',
        'image',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'catagory',
        'sub_catagory',
        'product_unit',
        'status',
        'returned',
        'damaged',
        'image',
    )
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}
    date_hierarchy = 'created_at'
