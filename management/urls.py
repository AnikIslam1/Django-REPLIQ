from django.urls import path
from . import views
#urls file added for rest view
urlpatterns = [
    path('company/<int:pk>', views.EmployeeViewSet.as_view()),
    path('company/<int:pk>/status', views.SubscriptionViewSet.as_view()),
]