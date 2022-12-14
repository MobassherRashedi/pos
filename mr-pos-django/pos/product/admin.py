from django.contrib import admin
from .models import Product,ProductImages,ProductUnitType

admin.site.register(ProductImages)
admin.site.register(ProductUnitType)
admin.site.register(Product)