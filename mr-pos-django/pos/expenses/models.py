from django.db import models
from pos.g_model import TimeStampMixin
from django.utils.translation import gettext as _
from datetime import datetime
# from settings.models import Catagory,SubCatagory 

class ExpensesCatagory(TimeStampMixin):
    name = models.CharField(max_length=150,blank=False, null=False)
    
    class Meta:
        verbose_name = _('Expens Catagory')
        verbose_name_plural = _('Expense Category')
        
    def __str__(self) -> str:
        return f"{self.id}"

class ExpensesSubCatagory(TimeStampMixin):
    name = models.CharField(max_length=150,blank=False, null=False)
    catagory = models.ForeignKey(ExpensesCatagory, on_delete= models.CASCADE)

    class Meta:
        verbose_name = _('Expense Sub Catagory')
        verbose_name_plural = _('Expense Sub Category')
        
    def __str__(self) -> str:
        return f"{self.id}"

class Expenses(TimeStampMixin):
    name = models.CharField(max_length=150, blank=False, null=False)
    date = models.DateTimeField(blank=False,null=True,default=datetime.now())
    catagory = models.ForeignKey(ExpensesCatagory, on_delete= models.CASCADE)
    sub_catagory = models.ForeignKey(ExpensesSubCatagory, on_delete= models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    note = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = _('Expense')
        verbose_name_plural = _('Expense')
        
    def __str__(self) -> str:
        return f"{self.id}"