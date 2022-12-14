from django.db import models
from pos.g_model import TimeStampMixin
from settings.models import Customer
from product.models import Product
from accounts.models import User
from django.utils.translation import gettext as _



#=========================================#
# Common  table start
#=========================================#
def get_invoice_number():
    # result = str(123).zfill(5) out: '00123' usecase: Add zeros to the left of the string
    import random
    numbers = [random.randint(1, 9) for _ in range(9)]
    res = 'INV'.join(str(numbers))
    return res

#=========================================#
# Common  table start
#=========================================#


#=========================================#
# Cart related table start
#=========================================# 

class SalesCart(TimeStampMixin):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sales_rate = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
                
    class Meta:
        verbose_name = _('Sales Cart')
        verbose_name_plural = _('Sales Cart')
      
    def __str__(self):
        return self.id

class SalesCartAmount(TimeStampMixin):
    cart = models.OneToOneField(SalesCart, on_delete=models.CASCADE)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    vat = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)
    vat_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    discount = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    Transport = models.DecimalField(max_digits=4, decimal_places=2,default=0.00) # add default amount
    total = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    paid =  models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    due =  models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
                
    class Meta:
        verbose_name = _('Sales Cart Amount')
        verbose_name_plural = _('Sales Cart Amount')
      
    def __str__(self) -> str:
        return f'{self.id}'
#=========================================#
# Cart related table end
#=========================================# 

#=========================================#
# Sales related table start
#=========================================# 
class Sales(TimeStampMixin):
    invoice_no = models.CharField(max_length=15,blank=False,null=False,default=get_invoice_number,editable=False)
    purchased_by = models.ForeignKey(User, on_delete=models.CASCADE,editable=False)
    barcode = models.CharField(max_length=50,blank=True,null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16,blank=True,null=True)
    address = models.CharField(max_length=150,blank=True,null=True)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    sales_rate = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False) # should foreign key
    qty = models.PositiveIntegerField()
    stock = models.PositiveIntegerField() # should foreign key
    totla_for_specific_item = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False,default=0.00)
    returened = models.BooleanField(default=False)
                
    class Meta:
        verbose_name = _('Sales')
        verbose_name_plural = _('Sales')
      
    def __str__(self) -> str:
        return f'{self.id}'
#=========================================#
# Sales related table start
#=========================================# 