
from django.db import models

class Tata(models.Model):
    Name=models.CharField(max_length= 30)
    Email=models.EmailField()
    Price=models.IntegerField()
    Model=models.DateField()
    Chassis=models.CharField(max_length=30)
