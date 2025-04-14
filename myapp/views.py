from django.shortcuts import render, get_object_or_404
from .models import Cliente, Vendedor, Producto, Pedido, PedidoProducto, Proveedor, Compra, CompraProducto

# Create your views here.
def index(request):
    context = {"mensaje": "Las mejores marcas traídas de todo el mundo"}
    return render(request, "myapp/index.html", context)

def clientes(request):
    clientes = Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, "myapp/clientes.html", context)

def vendedores(request):
    vendedores = Vendedor.objects.all()
    context = {"vendedores": vendedores}
    return render(request, "myapp/vendedores.html", context)

def productos(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, "myapp/productos.html", context)

def pedidos(request):
    pedidos = Pedido.objects.all()
    pedidos_data = []
    for pedido in pedidos:
        productos = pedido.pedidoproducto_set.all()
        total = pedido.calcular_total()
        pedidos_data.append({
            "pedido": pedido,
            "productos": productos,
            "total": total,
        })
    context = {"pedidos_data": pedidos_data}
    return render(request, "myapp/pedidos.html", context)

def proveedores(request):
    proveedores = Proveedor.objects.all()
    context = {"proveedores": proveedores}
    return render(request, "myapp/proveedores.html", context)

def compras(request):
    compras = Compra.objects.all()
    compras_data = []
    for compra in compras:
        productos = compra.compraproducto_set.all()
        total = compra.calcular_total()
        compras_data.append({
            "compra": compra,
            "productos": productos,
            "total": total,
        })
    context = {"compras_data": compras_data}
    return render(request, "myapp/compras.html", context)

def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    context = {"cliente": cliente}
    return render(request, "myapp/detalle_cliente.html", context)

def detalle_vendedor(request, vendedor_id):
    vendedor = get_object_or_404(Vendedor, id=vendedor_id)
    context = {"vendedor": vendedor}
    return render(request, "myapp/detalle_vendedor.html", context)

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    context = {"producto": producto}
    return render(request, "myapp/detalle_producto.html", context)

def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    context = {"pedido": pedido}
    return render(request, "myapp/detalle_pedido.html", context)

def detalle_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    context = {"proveedor": proveedor}
    return render(request, "myapp/detalle_proveedor.html", context)

def detalle_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    context = {"compra": compra}
    return render(request, "myapp/detalle_compra.html", context)

