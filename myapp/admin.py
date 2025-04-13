from django.contrib import admin
from models import Cliente, Producto, Pedido, Vendedor, Proveedor, PedidoProducto, Compra, CompraProducto, Factura, Pago, Devolucion, Inventario
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Vendedor)
admin.site.register(Proveedor)
admin.site.register(PedidoProducto)
admin.site.register(Compra)
admin.site.register(CompraProducto)
admin.site.register(Factura)
admin.site.register(Pago)
admin.site.register(Devolucion)
admin.site.register(Inventario)