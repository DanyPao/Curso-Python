from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, default='Pendiente', choices=[('Pendiente', 'Pendiente'), ('Completado', 'Completado'), ('Cancelado', 'Cancelado')])
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    productos = models.ManyToManyField(Producto, through='PedidoProducto')

    def calcular_total(self):
        total = 0
        for pedido_producto in self.pedidoproducto_set.all():
            total += pedido_producto.producto.precio * pedido_producto.cantidad
        return total

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nombre} {self.cliente.apellido}"
    
class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en {self.pedido}"

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    productos = models.ManyToManyField(Producto, through='CompraProducto')

    def calcular_total(self):
        total = 0
        for compra_producto in self.compraproducto_set.all():
            total += compra_producto.producto.precio * compra_producto.cantidad
        return total

    def __str__(self):
        return f"Compra {self.id} - {self.proveedor.nombre}"
  
class CompraProducto(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en {self.compra}"
class Factura(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Factura {self.id} - {self.pedido.cliente.nombre} {self.pedido.cliente.apellido}"
    
class Pago(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pago {self.id} - {self.factura.pedido.cliente.nombre} {self.factura.pedido.cliente.apellido}"
    
class Devolucion(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    fecha_devolucion = models.DateTimeField(auto_now_add=True)
    motivo = models.TextField()

    def __str__(self):
        return f"Devolución {self.id} - {self.pedido.cliente.nombre} {self.pedido.cliente.apellido}"

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cantidad} unidades de {self.producto.nombre}"


