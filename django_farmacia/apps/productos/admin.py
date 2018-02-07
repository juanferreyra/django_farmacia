from django.contrib import admin
from .models import Producto


class AdminProductos(admin.ModelAdmin):
    list_display = ['id', 'codigo', 'nombre', 'activo', 'fecha_creacion']
    search_fields = ['codigo', 'nombre']
    list_filter = ['activo']
    list_editable = ['nombre']

    class Meta:
        model = Producto


# Register your models here.
admin.site.register(Producto, AdminProductos)