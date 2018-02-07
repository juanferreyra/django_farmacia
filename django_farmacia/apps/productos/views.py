from django.shortcuts import render
from .models import Producto
from django.http import HttpResponse


# Create your views here.
def list(request):
    listado_de_productos = Producto.objects.all()
    return render(request, 'list.html', {'productos': listado_de_productos})


def producto_id(request, prod_id):
    product = Producto.objects.get(pk=prod_id)
    return render(request, 'detail.html', {'producto': product})
