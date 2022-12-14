from django.db import models
from pos.g_model import TimeStampMixin
from datetime import datetime
from django.utils.translation import gettext as _

#=========================================#
# Common  table start
#=========================================#
def get_unique_code(title):
    # result = str(123).zfill(5) out: '00123' usecase: Add zeros to the left of the string
    import random
    numbers = [random.randint(1, 9) for _ in range(6)]
    if title == 'product':
        res = 'P'.join(str(numbers))
    if title == 'customer':
        res = 'C'.join(str(numbers))
    if title == 'supplier':
        res = 'S'.join(str(numbers))
    return res

def get_upload_directory(instance, filename):
    # Generate the upload directory based on the current date
    return f"logo/{datetime.now().strftime('%Y/%m/%d')}"
#=========================================#
# Common  table start
#=========================================#

#=========================================#
# Product related table start
#=========================================# 

class Catagory(TimeStampMixin):
    name = models.CharField(max_length=50, blank=False, null=False)
    status = models.BooleanField(default=True)
                    
    class Meta:
        verbose_name = _('Catagory')
        verbose_name_plural = _('Catagory')
      
    def __str__(self) -> str:
        return f"{self.name}"

class SubCatagory(TimeStampMixin):
    name = models.CharField(max_length=50, blank=False, null=False)
    catagory = models.ForeignKey(Catagory, related_name='sub_catagory' ,on_delete=models.PROTECT)
    status = models.BooleanField(default=True)
                    
    class Meta:
        verbose_name = _('Sub Catagory')
        verbose_name_plural = _('Sub Catagory')
      
    def __str__(self) -> str:
        return f"{self.name}"

    
#=========================================#
# Customer related table start
#=========================================# 
class Customer(TimeStampMixin):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    customer_code = models.CharField(max_length=10, blank=False, null=False,unique=True,default=get_unique_code('customer'))
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_1 = models.CharField(max_length=16, blank=True, null=True)
    phone_2 = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    previous_due = models.DecimalField(max_digits=7,decimal_places=2,default=00000.00, blank=False, null=False)
                
    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customer')
      
    def __str__(self) -> str:
        return f"{self.name}"
    
#=========================================#
# Customer related table end
#=========================================# 


#=========================================#
# Supplier related table start
#=========================================# 
class Supplier(TimeStampMixin):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    supplier_code = models.CharField(max_length=10, blank=False, null=False,unique=True,default=get_unique_code('supplier'))
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_1 = models.CharField(max_length=16, blank=True, null=True)
    phone_2 = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    previous_due = models.DecimalField(max_digits=7,decimal_places=2,default=00000.00, blank=False, null=False)
              
    class Meta:
        verbose_name = _('Supplier')
        verbose_name_plural = _('Supplier')
      
    def __str__(self) -> str:
        return f"{self.name}"
    
#=========================================#
# Supplier related table end
#=========================================# 

#=========================================#
# Company related table start
#=========================================#
class CompanyInfo(TimeStampMixin):
    MY_CHOICES = (
        ('A4 Size', 'A4 Size'),
        ('1/2 of A4 Size', '1/2 of A4 Size'),
        ('POS', 'POS'),
    )
    name = models.CharField(max_length=100, blank=False, null=False)
    moto = models.CharField(max_length=150, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_1 = models.CharField(max_length=16, blank=True, null=True)
    phone_2 = models.CharField(max_length=16, blank=True, null=True)
    bin = models.CharField(max_length=20, blank=True, null=True)
    logo = models.ImageField(upload_to=get_upload_directory)
    email = models.EmailField(max_length=254, blank=True, null=True)
    invoice_print_type = models.CharField(max_length=15, choices=MY_CHOICES,default='POS')
                    
    class Meta:
        verbose_name = _('Company Info')
        verbose_name_plural = _('Company Info')
      
    def __str__(self) -> str:
        return f"{self.name}"
#=========================================#
# Company related table end
#=========================================# 
