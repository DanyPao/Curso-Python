from django.forms import Form, ModelForm, CharField, EmailField, IntegerField, DecimalField, Textarea, Select
from .models import Vendedor, Producto, Proveedor, Compra

class FormVendedor(ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nombre', 'apellido', 'email', 'telefono']

class FormProducto(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'proveedor']

class FormProveedor(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'contacto', 'telefono', 'email']

class FormCompra(ModelForm):
    class Meta:
        model = Compra
        fields = ['proveedor', 'precio', 'estado'] 
        