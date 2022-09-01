from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Usuario(models.Model):
    id_user = models.ForeignKey('auth.User', on_delete=models.CASCADE,null=True)

class Tipo_inmueble(models.Model):
    tipo_inmueble = models.TextField()
    
class Tipo_user(models.Model):
    tipo_user = models.TextField()

class Comuna(models.Model):
    comuna = models.TextField()

class Region(models.Model):
    region = models.TextField()
    
class Inmueble(models.Model):
    id_user = models.ForeignKey('auth.User', on_delete=models.CASCADE,null=True)
    id_tipo_inmueble = models.ForeignKey('m7_python.Tipo_inmueble', on_delete=models.CASCADE, null=True)
    id_comuna = models.ForeignKey('m7_python.Comuna', on_delete=models.CASCADE,null=True)
    id_region = models.ForeignKey('m7_python.Region', on_delete=models.CASCADE,null=True)
    nombre_inmueble = models.TextField()
    descripcion = models.CharField(max_length=300,null= False, blank=False)
    m2_construidos = models.FloatField(null= False, blank=False)
    m2_terreno = models.FloatField(null= False, blank=False)
    numero_estacionamientos = models.IntegerField(default= 0)
    numero_banios = models.IntegerField(default= 1)
    numero_habitaciones = models.IntegerField(default=1)
    direccion = models.CharField(max_length=300,null= False, blank=False)
   
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_tipo_user = models.ForeignKey('m7_python.Tipo_user', on_delete=models.CASCADE, null=True)
    rut = models.CharField(max_length=50,null= False, blank=False)
    direccion = models.CharField(max_length=300,null= False, blank=False)
    telefono = models.CharField(max_length=12)
    email = models.EmailField()

class Contactform(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4,editable=False)
    customer_email = models.EmailField(null=True)
    customer_name = models.CharField(max_length=64)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=1000)
    
def __str__(self):
    return f'{self.contact_form_uuid} {self.customer_name} {self.customer_email} {self.subject} {self.message}'