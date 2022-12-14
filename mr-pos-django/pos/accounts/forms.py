from django import forms

from .models import User,CustomerTransaction,SupplierTransaction

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = "__all__"
        # form class and attr in here

class CustomerTransactionForm(forms.ModelForm):
	class Meta:
		model = CustomerTransaction
		fields = "__all__"
        # form class and attr in here
    
class SupplierTransactionForm(forms.ModelForm):
	class Meta:
		model = SupplierTransaction
		fields = "__all__"
        # form class and attr in here
        
