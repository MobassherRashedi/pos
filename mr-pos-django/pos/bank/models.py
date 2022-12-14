from django.db import models
from pos.g_model import TimeStampMixin
from django.utils.translation import gettext as _

class Bank(TimeStampMixin):
    name = models.CharField(max_length=150,blank=False,null=False)
    account_name = models.CharField(max_length=150,blank=False,null=False)
    account_number = models.CharField(max_length=50,blank=False,null=False)
    branch = models.CharField(max_length=150,blank=False,null=False)
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True,default=0.00)
    
    class Meta:
        verbose_name = _('Bank')
        verbose_name_plural = _('Bank')
        
    def __str__(self) -> str:
        return f"{self.id}"

class BankTransactionType(TimeStampMixin):
    name = models.CharField(max_length=150,blank=False,null=False)
    
    class Meta:
        verbose_name = _('Bank Transaction Type')
        verbose_name_plural = _('Bank Transaction Type')
        
    def __str__(self) -> str:
        return f"{self.id}"

class BankTransaction(TimeStampMixin):
    bank_account = models.ForeignKey(Bank, on_delete=models.CASCADE)
    bank_transaction_type = models.ForeignKey(BankTransactionType, on_delete=models.CASCADE)
    branch = models.CharField(max_length=250,blank=True,null=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    
    class Meta:
        verbose_name = _('Bank Transactions')
        verbose_name_plural = _('Bank Transaction')
        
    def __str__(self) -> str:
        return f"{self.id}"
    
