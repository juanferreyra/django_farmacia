from django.db import models
from datetime import datetime


# Create your models here.
class Deposito(models.Model):
    codigo = models.CharField(max_length=80, blank=False, null=False, unique=True)
    nombre = models.CharField(max_length=80, blank=False, null=False)
    fecha_creacion = models.DateTimeField(default=datetime.now)
    fecha_modificacion = models.DateTimeField(default=datetime.now)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return 'Cliente (%d) %s' % (self.id, self.codigo)
