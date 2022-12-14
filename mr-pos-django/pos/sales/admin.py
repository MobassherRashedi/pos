from django.contrib import admin

from .models import SalesCart,SalesCartAmount,Sales


admin.site.register(SalesCart)
admin.site.register(SalesCartAmount)
admin.site.register(Sales)