from django.contrib import admin

from .models import Catagory,SubCatagory,Customer,CompanyInfo,Supplier

admin.site.register(Catagory)
admin.site.register(SubCatagory)
admin.site.register(Customer)
admin.site.register(CompanyInfo)
admin.site.register(Supplier)