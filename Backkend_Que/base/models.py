from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    rollno = models.CharField(max_length=200)
    age = models.IntegerField()
    branch = models.CharField(max_length=100)
    dob = models.DateField(max_length=100)
