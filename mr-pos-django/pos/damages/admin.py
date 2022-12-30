from django.contrib import admin

from .models import Damages


@admin.register(Damages)
class DamagesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'date',
        'product',
        'damage_qty',
        'amount',
        'note',
    )
    list_filter = ('created_at', 'updated_at', 'date', 'product')
    date_hierarchy = 'created_at'
