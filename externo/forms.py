from django.forms import Form, ModelForm, CharField, EmailField, IntegerField, DecimalField, Textarea, Select
from .models import Cliente, Pedido, PedidoProducto

class FormCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono']  

class FormPedido(ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'vendedor', 'estado']

class FormPedidoProducto(ModelForm):    
    class Meta:
        model = PedidoProducto
        fields = ['pedido', 'producto', 'cantidad']