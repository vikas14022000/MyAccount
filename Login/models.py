from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30,default="")
    last_name = models.CharField(max_length=30,default="")
    email = models.EmailField(unique=True,max_length=30,default="")
    userName = models.CharField(max_length=30,default="")
    password = models.CharField(max_length=128,default="")
    
    