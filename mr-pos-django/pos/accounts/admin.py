from django.contrib import admin

from .models import User,CustomerTransaction,SupplierTransaction,UserProfile

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(CustomerTransaction)
admin.site.register(SupplierTransaction)