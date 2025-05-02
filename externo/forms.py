from django.forms import Form, ModelForm, CharField, EmailField, IntegerField, DecimalField, Textarea, Select
from .models import Cliente, Pedido, PedidoProducto, Avatar
from django.contrib.auth.models import User
from django import forms

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

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
        
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        