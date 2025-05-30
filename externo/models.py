from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid

def generate_code():
    for i in range(32):
        code = uuid.uuid4().hex
        if not Cliente.objects.filter(code=code).exists():
            return code
    raise Exception("No se pudo generar un código único después de 32 intentos.")
# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    code = models.CharField(max_length=32, default=generate_code, editable=False, unique=True, db_index=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def get_absolute_url(self):
        return reverse("cbv_detalle_cliente", kwargs={"pk": self.pk})        

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey("interno.Vendedor", on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Completado', 'Completado')])
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def calcular_total(self):
        total = 0
        for pedido_producto in self.pedidoproducto_set.all():
            total += pedido_producto.producto.precio * pedido_producto.cantidad
        return total

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nombre}"
    
class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey("interno.Producto", on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en {self.pedido}"

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares/', null=True, blank=True)
    
    def __str__(self):
        return f"Avatar de {self.user.nombre} - {self.imagen}"



