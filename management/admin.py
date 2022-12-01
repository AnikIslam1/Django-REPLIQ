from django.contrib import admin

# Register your models here.
from .models import Company
from .models import Employee

class CompanyAccount(admin.ModelAdmin):
    list_display = ('pk','company_name','company_status')
admin.site.register(Company, CompanyAccount)

class EmployeeAccount(admin.ModelAdmin):
    list_display = ('pk','employee_name')
admin.site.register(Employee, EmployeeAccount)