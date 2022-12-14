from django.contrib import admin

from .models import User,CustomerTransaction,SupplierTransaction

admin.site.register(User)
admin.site.register(CustomerTransaction)
admin.site.register(SupplierTransaction)