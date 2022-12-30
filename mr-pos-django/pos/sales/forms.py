from django import forms


from .models import SalesCart, SalesCartAmount, Sales

class SalesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].widget.attrs.update({'aria-describedby':"id_sales-customer"})
        self.fields['invoice_no'].widget.attrs.update({'readonly':"true"})
        self.fields['purchased_by'].widget.attrs.update({'readonly':"true"})
        # self.fields['customer'].widget.attrs.update({'url':"{% url '' %}"}) 
        self.fields['date'].widget.attrs.update({'readonly':"true"})
        self.fields['stock'].widget.attrs.update({'readonly':"true"})
        self.fields['sales_rate'].widget.attrs.update({'readonly':"true"})
    class Meta:
        model = Sales
        fields = ["invoice_no","purchased_by","barcode","product","customer","phone","address","sales_rate","qty","stock","totla_for_specific_item","date"]
        readonly_fields = ['purchased_by']
        
class SalesCartForm(forms.ModelForm):
	class Meta:
		model = SalesCart
		fields = ["user","product","quantity","total_amount"]
        # form class and attr in here

class SalesCartAmountForm(forms.ModelForm):
	class Meta:
		model = SalesCartAmount
		fields = ['cart','sub_total','vat','vat_amount','discount','discount_amount','Transport','total','paid','due']
        # form class and attr in here
