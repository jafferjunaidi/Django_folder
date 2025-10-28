from django.db import models

# Create your models here.
class Student(models.Model):
    std_name = models.CharField(max_length=50)
    std_age = models.IntegerField() 
    std_city = models.CharField(max_length=50)
    std_mail = models.EmailField(max_length=60)           