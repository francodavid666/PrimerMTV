from operator import truediv
from django.db import models
from datetime import datetime

# Create your models here.
from mailbox import NoSuchMailboxError
from pyexpat import model



# Create your models here.
class familiar_1(models.Model):
     nombre= models.CharField(max_length=50)
     apellido = models.CharField(max_length=50)
     edad = models.IntegerField()
     fecha = datetime.today() # anio, mes, dia
     feca_nacimiento = models.DateField()
     
     
     
