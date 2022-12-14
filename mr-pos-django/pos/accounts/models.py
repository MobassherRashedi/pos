from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from pos.g_model import TimeStampMixin
from datetime import datetime
from django.urls import reverse,reverse_lazy
from settings.models import Customer,Supplier
from bank.models import BankTransactionType


#=========================================#
# Common info start
#=========================================#
def get_transaction_id():
    # result = str(123).zfill(5) out: '00123' usecase: Add zeros to the left of the string
    import random
    numbers =  ''.join([str(random.randint(1,9)) for _ in range(7)])
    res = 'TR'+(numbers)
    return res

# image upload for employee
def get_upload_directory(instance, filename):
    # Generate the upload directory based on the current date
    return f"images/profile/{instance.user.id}/{datetime.now().strftime('%Y/%m/%d')}"
#=========================================#
# Common info end
#=========================================#  

#=========================================#
# Usetr  related table start
#=========================================#
class User(AbstractUser):
    email = models.EmailField(max_length=255,unique=True)
    phone_number = PhoneNumberField(_("Phone number"),blank=True)
    password = models.CharField(_('Password'),max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_1 = models.CharField(max_length=16, blank=True, null=True)
    phone_2 = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True,unique=True)
    status = models.BooleanField(default=False)
    # group = models.CharField(max_length=15,choices=Group.objects.all().values_list('name', 'name'),blank=True, null=True)
                    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('User')
        
    def get_absolute_url(self):
        return reverse('User', kwargs={'pk': self.pk})
    
    @property
    def full_name(self):
        "Returns the person's full name."
        return f"{self.first_name} {self.last_name}" 
    
    def __str__(self) -> str:
        return f"{self.id}-{self.email}"
    
  
class UserProfile(TimeStampMixin):
    GENDER_CHOICE =[
            ('','select a gender'), 
            ('male','male'), 
            ('female','female'), 
        ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    date_of_birth = models.DateTimeField(_("Date of Birth"), default=datetime.now(), blank=False, null=False)
    gender = models.CharField(max_length=20, blank=False, null=False, choices=GENDER_CHOICE, default='')
    profile_picture = models.ImageField(upload_to=get_upload_directory, height_field=None, width_field=None, max_length=None)
    status = models.BooleanField(default=True)
#=========================================#
# Usetr  related table start
#=========================================#



#=========================================#
# Customer Transaction related table start
#=========================================# 
class CustomerTransaction(TimeStampMixin):
    transaction_date = models.DateTimeField(default=datetime.now())
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=150,blank=False,null=False,editable=False)# auto filled from customer field
    due = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    transaction_id = models.CharField(max_length=15,blank=False,null=False,default=get_transaction_id) # unique field test should be done 
    transaction_type = models.ForeignKey(BankTransactionType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    note = models.CharField(max_length=250,blank=True,null=True)   
    
    class Meta:
        verbose_name = _('Customer Transaction')
        verbose_name_plural = _('Customer Transaction')

    def get_absolute_url(self):
        return reverse('CustomerTransaction', kwargs={'pk': self.pk})
    
    def __str__(self) -> str:
        return f"{self.id}"
    
#=========================================#
#  Customer Transaction  related table end
#=========================================# 

#=========================================#
# Supplier Transactionn related table start
#=========================================# 

class SupplierTransaction(TimeStampMixin):
    transaction_date = models.DateTimeField(default=datetime.now())
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=150,blank=False,null=False,editable=False)# auto filled from customer field
    due = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    transaction_id = models.CharField(max_length=15,blank=False,null=False,default=get_transaction_id) # unique field test should be done 
    transaction_type = models.ForeignKey(BankTransactionType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    note = models.CharField(max_length=250,blank=True,null=True)
    
    class Meta:
        verbose_name = _('Supplier Transaction')
        verbose_name_plural = _('Supplier Transaction')
    
    def get_absolute_url(self):
        return reverse('SupplierTransaction', kwargs={'pk': self.pk})
        
    def __str__(self) -> str:
        return f"{self.id}"
    
#=========================================#
#  Supplier Transaction  related table end
#=========================================# 