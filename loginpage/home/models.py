from django.db import models

# Create your models here.

class Register(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    username=models.CharField(max_length=20,default='')
    password=models.CharField(max_length=122)
    date=models.DateField()

    def __str__(self):
        return self.name