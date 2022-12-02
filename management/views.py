# Create your views here.
from rest_framework import generics
from .models import Company,Employee, Subscription
from .serializer import CompanySerializer,EmployeeSerializer,SubscriptionSerializer


# class CompanyViewSet(generics.ListCreateAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

class EmployeeViewSet(generics.ListCreateAPIView):
    def employes(request, pk):
        queryset = Employee.objects.get(id=pk)
        return (request)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class SubscriptionViewSet(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer