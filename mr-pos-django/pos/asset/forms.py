from django import forms
from .models import Asset

class AssetForm(forms.ModelForm):
	class Meta:
		model = Asset
		fields = ['date','name','amount','note']
        # form class and attr in here
