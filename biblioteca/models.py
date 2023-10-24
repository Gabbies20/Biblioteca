from django.utils import timezone
from django.db import models

# Create your models here.
class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    fecha_Creacion = models.DateField(null=True,blank=True)
    telefono = models.IntegerField(null=True,blank=True)
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    dni = models.CharField(max_length=9,unique=True)

class Libro(models.Model):
    IDIOMAS = [
        ('ES','Español'),
        ('EN','Ingles'),
        ('FR','Francés'),
        ('IT','Italiano'),
    ]
    nombre = models.CharField(max_length=200)
    idioma = models.CharField(
                            max_length=2,
                            choices = IDIOMAS,
                            default='ES',
    )
    isbn = models.TextField(max_length=50,unique=True)
    GENEROS = [
        ('Te','Terror'),
        ('CF','Ciencia Ficción'),
        ('Po','Poesía'),
        ('Mi','Mitología'),
        ('Te','Teatro'),
    ]
    genero = models.CharField(
                                max_length=20,
                                choices=GENEROS,
                                default='Po',
    )
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    biblioteca = models.ForeignKey(Biblioteca,on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=200,unique=True)
    puntos = models.FloatField(default=5.0,db_column="puntos_biblioteca")
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField(max_length=9,null=True,blank=True)
    dni = models.CharField(max_length=9,unique=True)
    libros = models.ManyToManyField(Libro, through='Prestamo',related_name='prestamos_libros')
    
class DatosCliente(models.Model):
    direccion = models.TextField()
    gustos = models.TextField()
    telefono = models.IntegerField()
    cliente = models.OneToOneField(Cliente,on_delete=models.CASCADE)
    

class Prestamo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro,on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(default=timezone.now)
