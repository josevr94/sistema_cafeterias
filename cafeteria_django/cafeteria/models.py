from django.db import models

# Create your models here.

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5,decimal_places=2)
    categoria = models.CharField(max_length=100)
    imagen = models.ImageField()
    
class Barista(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()
    foto = models.ImageField()
    
class Cafe(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100) 
    origen = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5,decimal_places=2)
    nivel_tostado = models.CharField(max_length=100)
    perfil_sabor = models.CharField(max_length=100) 
    
    
class Resena(models.Model):
    id = models.AutoField(primary_key= True)
    nombre_cliente = models.CharField(max_length=100)
    calificacion = models.IntegerField()   
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)   
    
class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100) 
    contacto = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    descripcion = models.TextField()


def __str__(self):
    return self.name
          