from django.urls import path
from .views import index, clientes, pedidos, detalle_cliente, detalle_pedido, crear_cliente, crear_pedido, buscar

urlpatterns = [
    path("", index, name="index"),
    path("clientes/", clientes, name="clientes"),
    path("pedidos/", pedidos, name="pedidos"),
    path("clientes/<int:cliente_id>/", detalle_cliente, name="detalle_cliente"),
    path("pedidos/<int:pedido_id>/", detalle_pedido, name="detalle_pedido"),
    path("crear_cliente/", crear_cliente, name="crear_cliente"),
    path("crear_pedido/", crear_pedido, name="crear_pedido"),
    path('buscar/', buscar, name='buscar'),
]