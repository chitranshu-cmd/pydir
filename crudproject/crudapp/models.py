from django.db import models

class Employee(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.IntegerField()

   
# Create your models here.
    def __str__(self):
        return self.fname
        