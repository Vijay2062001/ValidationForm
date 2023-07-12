from django.db import models

# Create your models here.

class Student_n(models.Model):
    sname=models.CharField(max_length=100)
    sage=models.IntegerField()