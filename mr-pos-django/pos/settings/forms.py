from django import forms

from .models import Catagory, SubCatagory, Customer, Supplier, CompanyInfo

class CatagoryForm(forms.ModelForm):
	class Meta:
		model = Catagory
		fields = "__all__"
        # form class and attr in here

class SubCatagoryForm(forms.ModelForm):
	class Meta:
		model = SubCatagory
		fields = "__all__"
        # form class and attr in here

class CustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_code'].widget.attrs.update({'readonly':"true"})
    class Meta:
        model = Customer
        fields = ['first_name','last_name','customer_code','address','phone_1','phone_2','email','previous_due']
        
class SupplierForm(forms.ModelForm):
	class Meta:
		model = Supplier
		fields = "__all__"
        # form class and attr in here

class CompanyInfoForm(forms.ModelForm):
	class Meta:
		model = CompanyInfo
		fields = "__all__"
        # form class and attr in here
