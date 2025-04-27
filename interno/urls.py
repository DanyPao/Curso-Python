from django.urls import path
from .views import (
    vendedores, productos, proveedores, compras, crear_vendedor, crear_producto, crear_proveedor, crear_compra,
    detalle_vendedor, detalle_producto, detalle_proveedor, detalle_compra
)

urlpatterns = [
    path("vendedores/", vendedores, name="vendedores"),
    path("productos/", productos, name="productos"),
    path("proveedores/", proveedores, name="proveedores"),
    path("compras/", compras, name="compras"),
    path("crear_vendedor/", crear_vendedor, name="crear_vendedor"),
    path("crear_producto/", crear_producto, name="crear_producto"),
    path("crear_proveedor/", crear_proveedor, name="crear_proveedor"),
    path("crear_compra/", crear_compra, name="crear_compra"),
    path("vendedores/<int:vendedor_id>/", detalle_vendedor, name="detalle_vendedor"),
    path("productos/<int:producto_id>/", detalle_producto, name="detalle_producto"),
    path("proveedores/<int:proveedor_id>/", detalle_proveedor, name="detalle_proveedor"),
    path("compras/<int:compra_id>/", detalle_compra, name="detalle_compra"),
]