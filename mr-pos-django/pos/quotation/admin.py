from django.contrib import admin
from .models import Quotation,QuotationCart,QuotationCartAmount

admin.site.register(Quotation)
admin.site.register(QuotationCart)
admin.site.register(QuotationCartAmount)