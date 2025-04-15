from django.forms import Form, ModelForm, CharField, EmailField, IntegerField, DecimalField, Textarea, Select
from .models import Cliente, Vendedor, Producto, Pedido, Proveedor, Compra

class FormCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono']  

class FormVendedor(ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nombre', 'apellido', 'email', 'telefono']

class FormProducto(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'proveedor']

class FormPedido(ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'vendedor', 'estado']

class FormProveedor(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'contacto', 'telefono', 'email']

class FormCompra(ModelForm):
    class Meta:
        model = Compra
        fields = ['proveedor', 'producto', 'cantidad', 'precio', 'estado'] 