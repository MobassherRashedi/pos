from django.contrib import admin

from .models import Designation, Department, Employee, EmployeeSalaryPayment


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'name')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'name')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'employee_id',
        'fullname',
        'phone',
        'email',
        'designation',
        'department',
        'join_date',
        'basic_salary',
        'health',
        'transport',
        'providend_fund',
        'tax',
        'gender',
        'date_of_birth',
        'nid_number',
        'father_name',
        'father_nid_number',
        'mother_name',
        'mother_nid_number',
        'present_address',
        'permanent_address',
        'picture',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'designation',
        'department',
        'join_date',
        'date_of_birth',
    )
    date_hierarchy = 'created_at'


@admin.register(EmployeeSalaryPayment)
class EmployeeSalaryPaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'employee',
        'basic_salary',
        'health',
        'transport',
        'providend_fund',
        'tax',
        'date',
        'salary_month_unique_for_year',
        'commission',
        'deduction',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'employee',
        'date',
        'salary_month_unique_for_year',
    )
    date_hierarchy = 'created_at'