from django.contrib import admin

# Register your models here.
from .models import Company
from .models import Employee
from .models import Device
#company account registration
class CompanyAccount(admin.ModelAdmin):
    list_display = ('pk','company_name','company_status')
admin.site.register(Company, CompanyAccount)
#employee account registration
class EmployeeAccount(admin.ModelAdmin):
    list_display = ('pk','employee_name')
admin.site.register(Employee, EmployeeAccount)
#device status registration
class DeviceStatus(admin.ModelAdmin):
    list_display = ('pk','device_name','device_status','device_given_date','device_received_date')
admin.site.register(Device, DeviceStatus)