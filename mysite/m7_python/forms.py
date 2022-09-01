from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import Comuna, Region, Inmueble, Contactform
from django.forms import ModelForm

class UserForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = 'on'
    
    first_name = forms.CharField(max_length=50)
    first_name.label = 'Nombre'
    last_name = forms.CharField(max_length=50)
    last_name.label = 'Apellido'
    email = forms.EmailField(max_length=50, widget=forms.EmailInput)
    email.label = 'Correo ELectrónico'
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    
    
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username','email','password1','password2')
        labels = {'username': _("Nombre de Usuario")}
       
class TipoForm(forms.Form):
    tipos = ((1, 'Arrendatario'),(2, 'Dueño'),)
    tipo = forms.ChoiceField(choices=tipos)
    rut = forms.CharField(label='RUT',max_length=10)
    direccion = forms.CharField(label='Direccion', max_length=100)
    telefono = forms.CharField(label='Teléfono', max_length=100)
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['first_name','last_name','email']    

class InmuebleForm(forms.Form):
    tipos = ((1,"Casa"),(2,"Departamento"), (3,"Parcela"), (4,"Estacionamiento"),(5,"Otro"))
    id_tipo_inmueble = forms.ChoiceField(choices=tipos)
    comunas = [(x.id, x.comuna) for x in list(Comuna.objects.filter())]
    
    def nombre_comuna(e):
        return e[1]
    comunas.sort(key=nombre_comuna)
    
    id_comuna = forms.ChoiceField(choices=comunas)
    regiones = [(x.id, x.region)for x in list(Region.objects.filter())]
    id_region = forms.ChoiceField(choices=regiones)
    nombre_inmueble = forms.CharField(label="Nombre Inmueble", max_length=100)
    descripcion = forms.CharField(label="Descripcion", max_length=100)
    m2_construidos = forms.CharField(label="m2 Construidos", max_length=100)
    numero_banios = forms.IntegerField(label="Número de baños")
    numero_habitaciones = forms.IntegerField(label="Número de Habitaciones")
    direccion = forms.CharField(label="Dirección", max_length=100)
    m2_terreno = forms.CharField(label="m2 Terreno", max_length=100)
    numero_estacionamientos = forms.CharField(label="Número de estacionamientos")
    
class InmueblesUpdateForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields =['nombre_inmueble', 'descripcion', 'm2_construidos','numero_banios', 'numero_habitaciones', 'direccion','m2_terreno','numero_estacionamientos']



class ContactformForm(forms.Form):
    customer_email = forms.EmailField(label='Correo electrónico')
    customer_name = forms.CharField(max_length= 64,label='Nombre')
    subject = forms.CharField(max_length=255, label='Asunto')
    message = forms.CharField(label='Mensaje')

class ContactFormModelForm(ModelForm):
    class Meta:
        model = Contactform
        fields = ['customer_email', 'customer_name', 'subject', 'message']