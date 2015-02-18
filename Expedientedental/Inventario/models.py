from django.db import models
from decimal import Decimal




# Realizar views cuando termine Ray

class Categoria(models.Model):
        nombre = models.CharField(max_length=50)
        
        def __unicode__(self):

                return '%s '% (self.nombre)



class Producto(models.Model):
        precio=models.IntegerField()
        categoria=models.ForeignKey(Categoria)
        nombre=models.CharField(max_length=60)
        descripcion=models.CharField(max_length=120)
        def __unicode__(self):
                return '%s '% (self.nombre)



        