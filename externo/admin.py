from django.contrib import admin
from .models import Cliente, Pedido, PedidoProducto
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(PedidoProducto)
