from rest_framework.serializers import ModelSerializer
from .models import Company,Employee,Device,Subscription
#For API Json/Html serializer creation for Company ,Employee,Device & Subscription
class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'company_id',
            'company_name',
        ]
class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'employee_id',
            'employee_name',
        ]
class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = [
            'Device_name',
        ]
class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            'employee_id',
            'device_id',
            'handed_out_status',
            'returned_back_status',
        ]