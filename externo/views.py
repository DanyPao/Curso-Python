from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Pedido, PedidoProducto
from interno.models import Producto
from .forms import FormCliente, FormPedido, FormPedidoProducto
from django.forms import inlineformset_factory
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    context = {"mensaje": "Las mejores marcas traídas de todo el mundo"}
    return render(request, "externo/index.html", context)

#def clientes(request):
#    clientes = Cliente.objects.all()
#   context = {"clientes": clientes}
#    return render(request, "externo/clientes.html", context)

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
    return render(request, "externo/pedidos.html", context)

#def crear_cliente(request):
#    if request.method == "POST":
#        form = FormCliente(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect("clientes")
#    else:
#        form = FormCliente()
#    context = {"form": form}
#    return render(request, "externo/crear_cliente.html", context)

def crear_pedido(request):
    PedidoProductoFormSet = inlineformset_factory(Pedido, PedidoProducto, form=FormPedidoProducto, extra=1, can_delete=False)

    if request.method == "POST":
        form_pedido = FormPedido(request.POST)
        formset = PedidoProductoFormSet(request.POST)

        if form_pedido.is_valid() and formset.is_valid():
            pedido = form_pedido.save()
            formset.instance = pedido
            formset.save()
            pedido.total = pedido.calcular_total()
            return redirect("pedidos")  
    else:
        form_pedido = FormPedido()
        formset = PedidoProductoFormSet()

    context = {
        "form_pedido": form_pedido,
        "formset": formset,
    }
    return render(request, "externo/crear_pedido.html", context)

#def detalle_cliente(request, cliente_id):
#    cliente = get_object_or_404(Cliente, id=cliente_id)
#    context = {"cliente": cliente}
#    return render(request, "externo/detalle_cliente.html", context)

def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    context = {"pedido": pedido}
    return render(request, "externo/detalle_pedido.html", context)

def buscar(request):
    query = request.GET.get('q', '')
    resultados = Producto.objects.filter(nombre__icontains=query) 
    return render(request, 'externo/resultados_busqueda.html', {'resultados': resultados, 'query': query})

class ClienteListView(ListView):
    model = Cliente
    template_name = "externo/cbv/cliente-list.html"
    context_object_name="cliente"


class ClienteCreateView(CreateView):
    model = Cliente
    fields = ["nombre", "apellido", "email", "telefono"]
    template_name = "externo/cbv/cliente-create.html"
    succes_url = reverse_lazy("cbv_lista_clientes")

class ClienteDetailView(DetailView):
    model = Cliente
    fields = ["nombre", "apellido", "email", "telefono"]
    template_name = "externo/cbv/cliente-detail.html"
    
class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ["nombre", "apellido", "email", "telefono"]
    template_name = "externo/cbv/cliente-update.html"
    success_url = "/externo/cbv/lista_clientes"

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "externo/cbv/cliente-delete.html"
    success_url = reverse_lazy("cbv_lista_clientes")
    


