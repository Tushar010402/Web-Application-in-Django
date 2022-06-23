

# Create your models here.
#class Contact(models.model):
    #First_Name = models.CharField(max_length=30)
    #Last_Name = models.CharField(max_length=30)
    #email = models.CharField(max_length=30)
    #phone = models.CharField(max_length=12)
    #desc = models.TextField()
    #date = models.DateField()
from django.db import models


class Contact(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()