from django.db import models

class Clientes(models.Model):
    Nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    tele=models.CharField(max_length=7)