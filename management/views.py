# Create your views here.
from rest_framework import generics
from .models import Company,Employee, Subscription
from .serializer import CompanySerializer,EmployeeSerializer,SubscriptionSerializer


# class CompanyViewSet(generics.ListCreateAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

#Rest API Vier for employee
class EmployeeViewSet(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
#Rest API Vier for Subscription
class SubscriptionViewSet(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer