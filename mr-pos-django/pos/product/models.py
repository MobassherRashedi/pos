from django.db import models
from pos.g_model import TimeStampMixin
from settings.models import Catagory,SubCatagory
from datetime import datetime
from django.utils.translation import gettext as _
from django.utils.text import slugify
  
#=========================================#
# Common info start
#=========================================#

def get_unique_code(title):
    # result = str(123).zfill(5) out: '00123' usecase: Add zeros to the left of the string
    import random
    numbers =  ''.join([str(random.randint(1,9)) for _ in range(7)])
    if title == 'product':
        res = 'P'+(numbers)
    if title == 'customer':
        res = 'C'+(numbers)
    if title == 'supplier':
        res = 'S'+(numbers)
    return res

# image upload for employee
def get_upload_directory(instance, filename):
    # Generate the upload directory based on the current date
    return f"images/product/{datetime.now().strftime('%Y/%m/%d')}"
#=========================================#
# Common info end
#=========================================#  

#=========================================#
# Product related table start
#=========================================# 

class ProductImages(TimeStampMixin):
    file = models.ImageField(upload_to=get_upload_directory, height_field=None, width_field=None, max_length=None)
    status = models.BooleanField(default=True)
        
    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Image')
   
    def __str__(self) -> str:
        return f"{self.id}"

class ProductUnitType(TimeStampMixin):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=150, blank=True, null=True)
    status = models.BooleanField(default=True)
        
    class Meta:
        verbose_name = _('Product Unit Type')
        verbose_name_plural = _('Product Unit Type')
   
    def __str__(self) -> str:
        return f"{self.name}"

class Product(TimeStampMixin):
    name = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField(blank=False, null=False)
    product_code = models.CharField(max_length=10, blank=False, null=False,unique=True,default=get_unique_code('product'))
    catagory = models.ForeignKey(Catagory, related_name='products', on_delete=models.PROTECT)
    sub_catagory = models.ForeignKey(SubCatagory, related_name='products', on_delete=models.PROTECT)
    product_unit = models.ForeignKey(ProductUnitType, related_name='allproduct', on_delete=models.PROTECT)
    alert_qty = models.PositiveIntegerField(blank=False,null=False)
    purchase_rate = models.DecimalField(max_digits=7,decimal_places=2,default=00000.00, blank=False, null=False)
    sales_rate = models.DecimalField(max_digits=7,decimal_places=2,default=00000.00, blank=False, null=False)
    status = models.BooleanField(default=True)
    returened = models.BooleanField(default=False)
    damaged = models.BooleanField(default=False)
    image = models.ForeignKey(ProductImages, on_delete=models.CASCADE, blank=True, null=True)
    # stock = models.CharField(max_length=350, blank=True, null=True) # this sould be connected  with product model.
        
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Product')
   
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        "Returns slug field from name field and update automatically."
        self.slug = slugify(self.name)
        if update_fields is not None and "name" in update_fields:
            update_fields = {"slug"}.union(update_fields)
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )
   
    def __str__(self) -> str:
        return f"{self.name}"
    
#=========================================#
# Product related table end
#=========================================# 
