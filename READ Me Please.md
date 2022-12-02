##Django-REPLIQ
Django app to track corporate assets.

##Project Setup
  -Project name set to REPLIQ.
  -Application name set to management.
  -setting.py in REPLIQ added the application and rest_framework.
  -urls.py added admin panel name and title.
  -In urls.py added application API path for rest framework view.
  
##Supeadmin and user
  -Superuser considered as the developer company.
  -General user considered as the device holding company where dinamically permission is set by superuser 
    for create/update/delete operation of Employee, Device & Subscription details as required in task.
  -Only superadmin can creat a companyadmin for a perticular device holding company.

##models.py
  Four type of model is created for the operation
  - Company Model(which only can be created by Superadmin)
    In company model the Key relationship is set to one to one with the Django user outh for seperating other relationships with that perticular user.
    Also this model is considered as a parent model.
  - Employee Model
    This model is the child of company model.
    This model with its variable can be set by device company holder with specfic permission.
  - Device Model
    This model is the child of company model.
    This model with its variable can be set by device company holder with specfic permission.
  - Subscription Model
    This model is created with many to many relationship with Employee & Device.
    This model is the tracker where date time and status is included.
    
##admins.py
  -All models were required to register in admin for autentication and database creation.
  -Setting there admin panel view for each model.
 
##For RestAPI 
  -Extra file created in the application as named serializer and urls.
  -serializer.py ModelSerializer imported for rest serialization according to the models.py
  -Under the application urls.py rest view urls added  with general user primary key default.(company/<int:pk>)
  -Under the application urls.py rest view for subscription status urls has been added as 'company/<int:pk>/status'
  -In view.py some queryset added for viewing data. 
   But in some way we could restict the user to see other users data by taking primary key for that user by manipulating the query.
 
 
 
 
