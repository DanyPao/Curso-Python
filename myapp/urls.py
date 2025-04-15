from django.urls import path, include
from django.contrib import admin
from .views import index, clientes, vendedores, productos, pedidos, proveedores, compras, detalle_cliente, detalle_vendedor, detalle_producto, detalle_pedido, detalle_proveedor, detalle_compra, crear_cliente, crear_vendedor, crear_producto, crear_pedido, crear_proveedor, crear_compra, buscar
from django.conf import settings

urlpatterns = [
    path("", index, name="index"),
    path("clientes/", clientes, name="clientes"),
    path("vendedores/", vendedores, name="vendedores"),
    path("productos/", productos, name="productos"),
    path("pedidos/", pedidos, name="pedidos"),
    path("proveedores/", proveedores, name="proveedores"),
    path("compras/", compras, name="compras"),
    path("clientes/<int:cliente_id>/", detalle_cliente, name="detalle_cliente"),
    path("vendedores/<int:vendedor_id>/", detalle_vendedor, name="detalle_vendedor"),
    path("productos/<int:producto_id>/", detalle_producto, name="detalle_producto"),
    path("pedidos/<int:pedido_id>/", detalle_pedido, name="detalle_pedido"),
    path("proveedores/<int:proveedor_id>/", detalle_proveedor, name="detalle_proveedor"),
    path("compras/<int:compra_id>/", detalle_compra, name="detalle_compra"),
    path("crear_cliente/", crear_cliente, name="crear_cliente"),
    path("crear_vendedor/", crear_vendedor, name="crear_vendedor"),
    path("crear_producto/", crear_producto, name="crear_producto"),
    path("crear_pedido/", crear_pedido, name="crear_pedido"),
    path("crear_proveedor/", crear_proveedor, name="crear_proveedor"),
    path("crear_compra/", crear_compra, name="crear_compra"),
    path('buscar/', buscar, name='buscar'),
]