from django.contrib import admin
from .models import Department,Designation,Employee,EmployeeSalaryPayment


admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Employee)
admin.site.register(EmployeeSalaryPayment)

