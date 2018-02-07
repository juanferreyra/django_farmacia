from django.contrib import admin
from .models import Deposito


class AdminDeposito(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'fecha_creacion', 'activo']

    class Meta:
        model = Deposito


# Register your models here.
admin.site.register(Deposito, AdminDeposito)