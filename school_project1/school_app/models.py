from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=100)
    
    email=models.EmailField(unique=True)
    phonenumber=models.BigIntegerField(unique=True,null=True,blank=True)
    country=models.CharField(max_length=100)
    document=models.FileField(upload_to='documents/', null=True,blank=True)
    def __str__(self):
        return self.name
       
    

# Create your models here.
