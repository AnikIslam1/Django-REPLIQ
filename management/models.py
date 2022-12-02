from django.db import models

#importing auth.models for company andim user.
from django.contrib.auth.models import User
#Company model creation using auth.models usre or company admin assign from superadmin. 
class Company(models.Model):
  company_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  company_name = models.CharField(max_length=50)
  Contract = (('OnGoing','OnGoing'),('Expired','Expired'))
  contract_status = models.CharField(max_length=50, choices=Contract)
  def __str__(self):
    return self.company_name
#Employee model creation using Company models foreignKey
class Employee(models.Model):
    employee_id = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    employee_name = models.CharField(max_length=50)
    def __str__(self):
        return self.employee_name   

#Products or devices model creation
class Device(models.Model):
    device_id = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    device_name = models.CharField(max_length=50)
    def __str__(self):
        return self.device_name   
#Subscription for employees devices model creation
class Subscription(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE, null=True, blank=True)
    subscribed_by = models.CharField(max_length=50)
    Status = (('Best','Best'),('Good','Good'),('Poor','Poor'))
    handed_out_status = models.CharField(max_length=50, choices=Status)
    returned_back_status = models.CharField(max_length=50, choices=Status)
    subscription_open_date = models.DateTimeField(auto_now_add=True)
    subscription_close_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.handed_out_status   
