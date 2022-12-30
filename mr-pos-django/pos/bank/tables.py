import django_tables2 as tables
from .models import Bank,BankTransaction,BankTransactionType


class BankTable(tables.Table):
    name = tables.Column()
    account_name = tables.Column()
    account_number = tables.Column()
    branch = tables.Column()
    initial_balance = tables.Column()
    edit = tables.TemplateColumn(template_name='bank/partials/edit_button.html')
    delete = tables.TemplateColumn(template_name='bank/partials/delete_button.html')
    
    class Meta:
        model = Bank
        fields = ["name","account_name","account_number","branch","initial_balance"]
        attrs = {'class': 'table table-striped bank_table thead-dark ', 'id':'bankTable'}
        column_attrs = {
            'description': {'td': {'class': 'text-danger'}}
        }

class BankTransactionTypeTable(tables.Table):
    name = tables.Column()
    
    class Meta:
        model = BankTransactionType
        fields = ["name"]
        
        
class BankTransactionTable(tables.Table):
    bank_account = tables.Column()
    bank_transaction_type = tables.Column()
    branch = tables.Column()
    amount = tables.Column()
    
    class Meta:
        model = BankTransaction
        fields = ["bank_account","bank_transaction_type","branch","amount"]
