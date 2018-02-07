from django.db import models
from datetime import datetime
from apps.depositos.models import Deposito


# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(max_length=80, blank=False, null=False, unique=True)
    nombre = models.CharField(max_length=80, blank=False, null=False)
    stock_minimo = models.PositiveIntegerField(blank=False, null=False)
    precio_compra = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    precio_venta = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    deposito = models.ForeignKey(Deposito, on_delete=models.SET_NULL, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=datetime.now)
    fecha_modificacion = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return 'Producto (%s) %s ' % (self.codigo, self.nombre)
