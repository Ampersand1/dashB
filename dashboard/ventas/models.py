from django.db import models

# Create your models here.
class Dato(models.Model):
    mes = models.CharField(max_length=120)
    ventas = models.CharField(max_length=120)
    barrio = models.CharField(max_length=120)
