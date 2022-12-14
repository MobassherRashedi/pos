from django.db import models
from pos.g_model import TimeStampMixin
from datetime import datetime 
from django.utils.translation import gettext as _

  
#=========================================#
# Common info start
#=========================================#
def get_employee_id():
    # result = str(123).zfill(5) out: '00123' usecase: Add zeros to the left of the string
    import random
    numbers = [random.randint(1, 9) for _ in range(7)]
    res = 'EM'.join(str(numbers))
    return res

# image upload for employee
def get_upload_directory(instance, filename):
    # Generate the upload directory based on the current date
    return f"images/employee/{datetime.now().strftime('%Y/%m/%d')}"
#=========================================#
# Common info end
#=========================================#  


class Designation(TimeStampMixin):
    name = models.CharField(max_length=150, blank=False, null=False)

    class Meta:
        verbose_name = _('Designation')
        verbose_name_plural = _('Designation')
        
    def __str__(self) -> str:
        return f"{self.id}"
    
class Department(TimeStampMixin):
    name = models.CharField(max_length=150, blank=False, null=False)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Department')
        
    def __str__(self) -> str:
        return f"{self.id}"
    
class Employee(TimeStampMixin):
    GENDER_CHOICE =[
        ('male','male'),
        ('female','female'),
        ('not interested','not interested'),
    ]
    
    employee_id = models.CharField(max_length=12,blank=False,null=False,default=get_employee_id)
    fullname = models.CharField(max_length=150, blank=False, null=False)
    phone = models.CharField(max_length=16, blank=False, null=False)
    email = models.EmailField(max_length=255,blank=True,null=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    join_date = models.DateTimeField(default=datetime.now())
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    health = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    transport = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    providend_fund = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    tax = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    gender = models.CharField(max_length=20,blank=False,null=False,choices=GENDER_CHOICE)
    date_of_birth = models.DateTimeField(blank=True,null=True)
    nid_number = models.CharField(max_length=20, blank=True, null=True)
    father_name = models.CharField(max_length=150, blank=False, null=False)
    father_nid_number = models.CharField(max_length=20, blank=True, null=True)
    mother_name = models.CharField(max_length=150, blank=False, null=False)
    mother_nid_number = models.CharField(max_length=20, blank=True, null=True)
    present_address = models.CharField(max_length=200, blank=False, null=False)
    permanent_address = models.CharField(max_length=200, blank=False, null=False)
    picture = models.ImageField(upload_to=get_upload_directory)
    
    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employee')
        
    def __str__(self) -> str:
        return f"{self.id}"
    
class EmployeeSalaryPayment(TimeStampMixin):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    health = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    transport = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    providend_fund = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    tax = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    date = models.DateTimeField(blank=True,null=True, default=datetime.now())
    salary_month_unique_for_year = models.DateField(blank=False,null=False,unique=True,default=datetime.now())
    commission = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)
    deduction = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)
    
    class Meta:
        verbose_name = _('Employee Salary Payment')
        verbose_name_plural = _('Employee Salary Payment')
        
    def __str__(self) -> str:
        return f"{self.id}"
    