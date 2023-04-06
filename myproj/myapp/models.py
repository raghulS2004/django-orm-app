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