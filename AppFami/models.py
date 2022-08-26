from django.db import models

# Create your models here.
from mailbox import NoSuchMailboxError
from pyexpat import model



# Create your models here.
class familiar_1(models.Model):
     nombre= models.CharField(max_length=50)
     apellido = models.CharField(max_length=50)
     edad = models.IntegerField()
     
     
class familiar_2(models.Model):
      nombre= models.CharField(max_length=50)
      apellido = models.CharField(max_length=50)
      edad = models.IntegerField()  
      
     
    

class familiar_3(models.Model):
      nombre= models.CharField(max_length=50)
      apellido = models.CharField(max_length=50)
      edad = models.IntegerField()