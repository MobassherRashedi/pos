from django import forms

from .models import Bank,BankTransactionType,BankTransaction

class BankForm(forms.ModelForm):
	class Meta:
		model = Bank
		fields = ["name","account_name","account_number","branch","initial_balance"]
        # form class and attr in here

class BankTransactionTypeForm(forms.ModelForm):
	class Meta:
		model = BankTransactionType
		fields = ["name"]
        # form class and attr in here
        
class BankTransactionForm(forms.ModelForm):
	class Meta:
		model = BankTransaction
		fields = ["bank_account","bank_transaction_type","branch","amount"]
        # form class and attr in here