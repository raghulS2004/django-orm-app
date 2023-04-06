# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:
Fork and clone the repositary in to your IDE.
### STEP 2:
Create a django project and an app and a superuser account and run the server.
### STEP 3:
Modify changes in settings and write ur code on models and admin and run the server.
### STEP 4:
Login in to admin using your superuser account and populate the records.

## PROGRAM:
```
from django.db import models
from django.contrib import admin
# Create your models here.
class Laptop(models.Model):
    Productid= models.CharField(max_length=100,primary_key = True)
    Brandname = models.CharField(max_length=100)
    Modelname = models.CharField(max_length=80)
    Os = models.CharField(max_length=100)
    Colour = models.CharField(max_length=100)
    Price = models.IntegerField()

    
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('Productid','Brandname','Modelname','Os','Colour','Price')
```
## OUTPUT:

![r2](https://user-images.githubusercontent.com/122069938/230361271-aea11efa-b88b-4325-a93c-9d152d7713fa.jpg)
![r1](https://user-images.githubusercontent.com/122069938/230361290-8f9bda0f-563e-457d-8b01-9c7da7e9b666.jpg)

## RESULT
Thus we developed a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).
