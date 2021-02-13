from django.db import models

class Usuario(models.Model):
    name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True) #Se modifica solo al inicio.
    update_at = models.DateTimeField(auto_now=True) #Se modifica cada vez que se accede al dato.

# Create your models here.
