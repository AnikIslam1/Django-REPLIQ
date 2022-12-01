from django.db import models
#importing auth.models for company andim user.
from django.contrib.auth.models import User
#Company model creation using auth.models usre or company admin assign from superadmin. 
class Company(models.Model):
  company_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  company_name = models.CharField(max_length=50)
  company_status = ('Active')
  def __str__(self):
    return self.company_name
#Employee model creation using Company models foreignKey
class Employee(models.Model):
    employee_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.employee_name   
