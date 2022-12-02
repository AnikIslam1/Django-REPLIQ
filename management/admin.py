from django.contrib import admin

# Register your models here.
from .models import Company, Employee, Device, Subscription


#company account registration
class CompanyAccount(admin.ModelAdmin):
    list_display = ('pk','company_name','contract_status')
admin.site.register(Company, CompanyAccount)
#employee account registration
class EmployeeAccount(admin.ModelAdmin):
    list_display = ('pk','employee_name')
admin.site.register(Employee, EmployeeAccount)
#device status registration
class DeviceStatus(admin.ModelAdmin):
    list_display = ('pk','device_name')
admin.site.register(Device, DeviceStatus)
#Subscription status registration
class SubscriptionStatus(admin.ModelAdmin):
    list_display = ('pk','subscribed_by','handed_out_status','returned_back_status','subscription_open_date','subscription_close_date')
admin.site.register(Subscription, SubscriptionStatus)