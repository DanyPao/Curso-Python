from django.contrib import admin
from .models import Compra, CompraProducto, Producto, Proveedor, Vendedor
# Register your models here.
admin.site.register(Vendedor)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Compra)
admin.site.register(CompraProducto)