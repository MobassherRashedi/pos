from django import forms
from .models import ProductImages, ProductUnitType, Product


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name','slug','product_code','catagory','sub_catagory','product_unit','alert_qty','purchase_rate','sales_rate','status','returened','damaged','image']
        # form class and attr in here

# class ProductUnitTypeForm(forms.ModelForm):
# 	class Meta:
# 		model = ProductUnitType
# 		fields = "__all__"
#         # form class and attr in here

# class ProductImagesForm(forms.ModelForm):
# 	class Meta:
# 		model = ProductImages
# 		fields = "__all__"
#         # form class and attr in here
