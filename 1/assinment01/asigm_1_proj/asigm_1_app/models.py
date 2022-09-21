from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(int)
    address = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=11)