from django.db import models
from pos.g_model import TimeStampMixin
from settings.models import Customer
from accounts.models import User
from product.models import Product
from django.utils.translation import gettext as _



#=========================================#
# Common  table and extra info  start
#=========================================#
def get_invoice_number():
    # result = str(123).zfill(5) out: '00123' usecase: Add zeros to the left of the string
    import random
    numbers = [random.randint(1, 9) for _ in range(9)]
    res = 'Q-'.join(str(numbers))
    return res

#=========================================#
# Common  table and extra info  end
#=========================================#


#=========================================#
# Quotation Cart related table start
#=========================================# 

class QuotationCart(TimeStampMixin):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sales_rate = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
             
    class Meta:
        verbose_name = _('Quotation Cart')
        verbose_name_plural = _('Quotation Cart')
      
    def __str__(self):
        return self.id

class QuotationCartAmount(TimeStampMixin):
    cart = models.OneToOneField(QuotationCart, on_delete=models.CASCADE)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    vat = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)
    vat_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    discount = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
             
    class Meta:
        verbose_name = _('Quotation Cart Amount')
        verbose_name_plural = _('Quotation Cart Amount')
      
    def __str__(self) -> str:
        return f'{self.id}'
#=========================================#
# Quotation Cart related table end
#=========================================# 

#=========================================#
# Quotation related table start
#=========================================# 
class Quotation(TimeStampMixin):
    invoice_no = models.CharField(max_length=15,blank=False,null=False,default=get_invoice_number,editable=False)
    purchased_by = models.ForeignKey(User, on_delete=models.CASCADE,editable=False)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=150,blank=False,null=False)
    phone = models.CharField(max_length=16,blank=True,null=True)
    address = models.CharField(max_length=150,blank=True,null=True)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    sales_rate = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False) # should foreign key
    qty = models.PositiveIntegerField()
    stock = models.PositiveIntegerField() # should foreign key
    totla_for_specific_item = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False,default=0.00)
    returened = models.BooleanField(default=False)
         
    class Meta:
        verbose_name = _('Quotation')
        verbose_name_plural = _('Quotation')
    
    def __str__(self) -> str:
        return f'{self.id}'
#=========================================#
# Quotation related table start
#=========================================# 