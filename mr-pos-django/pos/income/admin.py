# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import IncomeCatagory, IncomeSubCatagory, Income


@admin.register(IncomeCatagory)
class IncomeCatagoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'name')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(IncomeSubCatagory)
class IncomeSubCatagoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'name', 'catagory')
    list_filter = ('created_at', 'updated_at', 'catagory')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'name',
        'date',
        'catagory',
        'sub_catagory',
        'amount',
        'note',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'date',
        'catagory',
        'sub_catagory',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'