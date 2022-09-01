from django.contrib import admin

from m7_python.models import Inmueble, Profile
from django.contrib import admin
from .models import Usuario

# Register your models here.
admin.site.register(Inmueble)
admin.site.register(Profile)
admin.site.register(Usuario)