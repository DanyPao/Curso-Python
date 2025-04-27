from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


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



