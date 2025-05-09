from django.db import models
import uuid

def generate_code():
    for i in range(32):
        code = uuid.uuid4().hex
        if not Vendedor.objects.filter(code=code).exists():
            return code
        elif not Proveedor.objects.filter(code=code).exists():
            return code
    raise Exception("No se pudo generar un código único después de 32 intentos.")
# Create your models here.
class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    code = models.CharField(max_length=32, default=generate_code, editable=False, unique=True, db_index=True)

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
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    code = models.CharField(max_length=32, default=generate_code, editable=False, unique=True, db_index=True)
    
    def __str__(self):
        return self.nombre

class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Completada', 'Completada')])

    def calcular_total(self):
        total = sum(
            item.producto.precio * item.cantidad for item in self.compraproducto_set.all()
        )
        return total

    def __str__(self):
        return f"Compra {self.id} - {self.proveedor.nombre}"
  
class CompraProducto(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en {self.compra}"
