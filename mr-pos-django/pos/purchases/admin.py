from django.contrib import admin

from .models import PurchaseCart,PurchaseCartAmount,Purchase


admin.site.register(PurchaseCart)
admin.site.register(PurchaseCartAmount)
admin.site.register(Purchase)