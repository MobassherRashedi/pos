from django.db import models
from pos.g_model import TimeStampMixin
from settings.models import Customer
from product.models import Product
from accounts.models import User
from django.utils.translation import gettext as _
from datetime import datetime 
import decimal


#=========================================#
# Common  table start
#=========================================#
def get_invoice_number():
    # result = str(123).zfill(5) out: '00123' usecase: Add zeros to the left of the string
    import random
    numbers =  ''.join([str(random.randint(1,9)) for _ in range(7)])
    res = 'INV'+(numbers)
    return res

#=========================================#
# Common  table start
#=========================================#


#=========================================#
# Cart related table start
#=========================================# 

class SalesCart(TimeStampMixin):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    active = models.BooleanField(_("active"), default=True)
    purchased = models.BooleanField(_("purchased"), default=False)
                
    class Meta:
        verbose_name = _('Sales Cart')
        verbose_name_plural = _('Sales Cart')
        
    def save(self, *args, **kwargs):
        self.total_amount = self.product.sales_rate * decimal.Decimal(self.quantity)
        super(SalesCart, self).save(*args, **kwargs)
      
    def __str__(self):
        return f"{self.id}"
    


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
    
    
    
# class Cart(models.Model):
#     # Field for storing the customer associated with the cart
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     # Field for storing the products in the cart
#     products = models.ManyToManyField(Product, through='CartProduct')

# class CartProduct(models.Model):
#     # Fields for storing the relationship between the cart and the products
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     # Field for storing the quantity of the product in the cart
#     quantity = models.PositiveIntegerField()

#=========================================#
# Cart related table end
#=========================================# 

#=========================================#
# Sales related table start
#=========================================# 
class Sales(TimeStampMixin):
    invoice_no = models.CharField(max_length=15,blank=False,null=False,default=get_invoice_number,editable=True)
    purchased_by = models.ForeignKey(User, on_delete=models.CASCADE,editable=True)
    barcode = models.CharField(max_length=50,blank=True,null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16,blank=True,null=True)
    address = models.CharField(max_length=150,blank=True,null=True)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    sales_rate = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False) # should foreign key
    qty = models.PositiveIntegerField()
    stock = models.PositiveIntegerField() # should foreign key
    totla_for_specific_item = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False,default=0.00)# total 
    returned = models.BooleanField(default=False)
    date = models.DateTimeField(_("date"), default=datetime.now(), blank=True, null=True)
                
    class Meta:
        verbose_name = _('Sales')
        verbose_name_plural = _('Sales')
      
    def __str__(self) -> str:
        return f'{self.id}'
    

#=========================================#
# Sales related table start
#=========================================# 

#=========================================#
# checkout related table start
#=========================================# 

# class Order(models.Model):
#     # Field for storing the cart associated with the order
#     cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
#     # Fields for storing the billing and shipping information for the order
#     billing_name = models.CharField(max_length=100)
#     billing_address = models.CharField(max_length=200)
#     billing_city = models.CharField(max_length=100)
#     billing_state = models.CharField(max_length=100)
#     billing_zip = models.CharField(max_length=10)
#     shipping_name = models.CharField(max_length=100)
#     shipping_address = models.CharField(max_length=200)
#     shipping_city = models.CharField(max_length=100)
#     shipping_state = models.CharField(max_length=100)
#     shipping_zip = models.CharField(max_length=10)
#     # Field for storing the total cost of the order
#     total_cost = models.DecimalField(max_digits=10, decimal_places=2)
#     # Other fields here...

# class Payment(models.Model):
#     # Field for storing the order associated with the payment
#     order = models.OneToOneField(Order, on_delete=models.CASCADE)
#     # Fields for storing payment information (e.g. payment method, transaction ID, etc.)
#     payment_method = models.CharField(max_length=100)
#     transaction_id = models.CharField(max_length=100)
#     # Other fields here...
#=========================================#
# checkout related table end
#=========================================# 