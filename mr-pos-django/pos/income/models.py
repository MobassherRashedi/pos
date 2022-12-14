from django.db import models
from pos.g_model import TimeStampMixin
from django.utils.translation import gettext as _
from datetime import datetime
# from settings.models import Catagory,SubCatagory 

class IncomeCatagory(TimeStampMixin):
    name = models.CharField(max_length=150,blank=False, null=False)
    
    class Meta:
        verbose_name = _('Income Catagory')
        verbose_name_plural = _('Income Catagory')
   
    def __str__(self) -> str:
        return f"{self.id}"

class IncomeSubCatagory(TimeStampMixin):
    name = models.CharField(max_length=150,blank=False, null=False)
    catagory = models.ForeignKey(IncomeCatagory, on_delete= models.CASCADE)
    
    class Meta:
        verbose_name = _('Income Sub Catagory')
        verbose_name_plural = _('Income Sub Catagory')
   
    def __str__(self) -> str:
        return f"{self.id}"

class Income(TimeStampMixin):
    name = models.CharField(max_length=150, blank=False, null=False)
    date = models.DateTimeField(blank=False,null=True,default=datetime.now())
    catagory = models.ForeignKey(IncomeCatagory, on_delete= models.CASCADE)
    sub_catagory = models.ForeignKey(IncomeSubCatagory, on_delete= models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    note = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = _('Income')
        verbose_name_plural = _('Income')
   
    def __str__(self) -> str:
        return f"{self.id}"