from django.db import models

#importing auth.models for company andim user.
from django.contrib.auth.models import User
#Company model creation using auth.models usre or company admin assign from superadmin. 
class Company(models.Model):
  company_name = models.CharField(max_length=50)
  company_status = ('Active')
  def __str__(self):
    return self.company_name
#Employee model creation using Company models foreignKey
class Employee(models.Model):
    
    employee_name = models.CharField(max_length=50)
    def __str__(self):
        return self.employee_name   

#Products or devices model creation
class Device(models.Model):
    device_name = models.CharField(max_length=50)
    device_status = models.CharField(max_length=50)
    device_given_date = models.DateField()
    device_received_date = models.DateField()
    def __str__(self):
        return self.Device_name   
