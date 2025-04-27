from django.shortcuts import render, get_object_or_404, redirect
from .models import Vendedor, Producto, Proveedor, Compra, CompraProducto
from .forms import FormVendedor, FormProducto, FormProveedor, FormCompra
from django.forms import inlineformset_factory
# Create your views here.
def vendedores(request):
    vendedores = Vendedor.objects.all()
    context = {"vendedores": vendedores}
    return render(request, "interno/vendedores.html", context)

def productos(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, "interno/productos.html", context)

def proveedores(request):
    proveedores = Proveedor.objects.all()
    context = {"proveedores": proveedores}
    return render(request, "interno/proveedores.html", context)

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
    return render(request, "interno/compras.html", context)

def crear_vendedor(request):
    if request.method == "POST":
        form = FormVendedor(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vendedores")
    else:
        form = FormVendedor()
    context = {"form": form}
    return render(request, "interno/crear_vendedor.html", context)

def crear_producto(request):
    if request.method == "POST":
        form = FormProducto(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos")
    else:
        form = FormProducto()
    context = {"form": form}
    return render(request, "interno/crear_producto.html", context)

def crear_proveedor(request):
    if request.method == "POST":
        form = FormProveedor(request.POST)
        if form.is_valid():
            form.save()
            return redirect("proveedores")
    else:
        form = FormProveedor()
    context = {"form": form}
    return render(request, "interno/crear_proveedor.html", context)

def crear_compra(request):
    CompraProductoFormSet = inlineformset_factory(Compra, CompraProducto, fields=('producto', 'cantidad'), extra=1, can_delete=False)

    if request.method == "POST":
        form = FormCompra(request.POST)
        formset = CompraProductoFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            compra = form.save()
            formset.instance = compra
            formset.save()
            return redirect("compras")
    else:
        form = FormCompra()
        formset = CompraProductoFormSet()

    context = {"form": form, "formset": formset}
    return render(request, "interno/crear_compra.html", context)

def detalle_vendedor(request, vendedor_id):
    vendedor = get_object_or_404(Vendedor, id=vendedor_id)
    context = {"vendedor": vendedor}
    return render(request, "interno/detalle_vendedor.html", context)

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    context = {"producto": producto}
    return render(request, "interno/detalle_producto.html", context)

def detalle_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    context = {"proveedor": proveedor}
    return render(request, "interno/detalle_proveedor.html", context)

def detalle_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    context = {"compra": compra}
    return render(request, "interno/detalle_compra.html", context)
