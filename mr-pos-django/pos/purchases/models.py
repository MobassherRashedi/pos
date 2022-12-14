from django.db import models
from pos.g_model import TimeStampMixin
from settings.models import Supplier,Catagory,SubCatagory
from accounts.models import User
from product.models import Product
from django.utils.translation import gettext as _



#=========================================#
# Common  table and function start
#=========================================#
def get_invoice_number():
    # result = str(123).zfill(5) out: '00123' usecase: Add zeros to the left of the string
    import random
    numbers = [random.randint(1, 9) for _ in range(9)]
    res = 'INV'.join(str(numbers))
    return res

#=========================================#
# Common  table and function end
#=========================================#


#=========================================#
# Cart related table start
#=========================================# 

class PurchaseCart(TimeStampMixin):
    user = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sales_rate = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
         
    class Meta:
        verbose_name = _('Purchase Cart')
        verbose_name_plural = _('Purchase Cart')
      
    def __str__(self):
        return self.id

class PurchaseCartAmount(TimeStampMixin):
    cart = models.OneToOneField(PurchaseCart, on_delete=models.CASCADE)
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
        verbose_name = _('Purchase Cart Amount')
        verbose_name_plural = _('Purchase Cart Amount')
        
    def __str__(self) -> str:
        return f'{self.id}'
#=========================================#
# Cart related table end
#=========================================# 

#=========================================#
# Sales related table start
#=========================================# 
class Purchase(TimeStampMixin):
    invoice_no = models.CharField(max_length=15,blank=False,null=False,default=get_invoice_number,editable=False)
    purchased_by = models.ForeignKey(User, on_delete=models.CASCADE,editable=False)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    sub_catagory = models.ForeignKey(SubCatagory, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    purchase_rate = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False) # should foreign key
    qty = models.PositiveIntegerField()
    sales_rate = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False) # should foreign key
    stock = models.PositiveIntegerField() # should foreign key
    totla_for_specific_item = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False,default=0.00)
    selling_price = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    returened = models.BooleanField(default=False)
           
    class Meta:
        verbose_name = _('Purchase')
        verbose_name_plural = _('Purchase')
    
    def __str__(self) -> str:
        return f'{self.id}'
#=========================================#
# Sales related table start
#=========================================# 