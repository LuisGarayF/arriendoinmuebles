from django.shortcuts import render
from m7_python.models import *
from m7_python.forms import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def registerView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_tipo?user='+str(form.cleaned_data['username']))
    else:
        form = UserForm()
        
    return render(request, 'registration/register.html',{'form': form})

def register_tipoView(request):
    username = request.GET['user']
    t_form =  TipoForm(request.POST or None)
    if request.method == 'POST':
       if t_form.is_valid():
        tipo = t_form.cleaned_data['tipo']
        rut = t_form.cleaned_data['rut']
        direccion = t_form.cleaned_data['direccion']
        telefono = t_form.cleaned_data['telefono']
        user = User.objects.filter(username=username)[0]
        id_tipo_user = Tipo_user.objects.filter(id=int(tipo))[0]
        
        datos = Profile(user=user, id_tipo_user=id_tipo_user, rut=rut, direccion=direccion, telefono=telefono)
        datos.save()
        
        return HttpResponseRedirect('/login/')

    else:
        form = TipoForm()
        return render(request, 'registration/register_tipo.html',{'form': form})

@login_required
def dashboardView(request):
    current_user = request.user
    Inm = Inmueble.objects.filter(id_user_id=current_user.id)
    tipoUser = Profile.objects.filter(user_id=current_user.id).first()
             
    return render(request,'dashboard.html', {'inmuebles': Inm , 'utipo': tipoUser.id_tipo_user_id})

def indexView(request):
    Inm = Inmueble.objects.all()
    return render(request,'index.html', {'inmuebles': Inm})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        u_form = UserUpdateForm(instance=request.user)
    
    return render(request,'update_profile.html',{'u_form': u_form})

@login_required
def new_inmuebleView(request):
    u_form = InmuebleForm(request.POST or None)
    if u_form.is_valid():
        id_tipo_inmueble = u_form.cleaned_data['id_tipo_inmueble']
        id_comuna = u_form.cleaned_data['id_comuna']
        id_region = u_form.cleaned_data['id_region']
        nombre_inmueble = u_form.cleaned_data['nombre_inmueble']
        descripcion = u_form.cleaned_data['descripcion']
        m2_construidos = u_form.cleaned_data['m2_construidos']
        numero_banios = u_form.cleaned_data['numero_banios']
        numero_habitaciones = u_form.cleaned_data['numero_habitaciones']
        direccion = u_form.cleaned_data['direccion']
        m2_terreno = u_form.cleaned_data['m2_terreno']
        numero_estacionamientos = u_form.cleaned_data['numero_estacionamientos']
           
        tipo_inmueble = Tipo_inmueble.objects.filter(id=int(id_tipo_inmueble))[0]
        comuna = Comuna.objects.filter(id=int(id_comuna))[0]
        reg = Region.objects.filter(id=int(id_region))[0]
        current_user = request.user
        user = User.objects.filter(id=current_user.id)
        inm = Inmueble(id_tipo_inmueble=tipo_inmueble,
                        id_comuna = comuna,
                        id_region = reg,
                        nombre_inmueble = nombre_inmueble,
                        descripcion = descripcion,
                        m2_construidos = m2_construidos,
                        numero_banios = numero_banios,
                        numero_habitaciones = numero_habitaciones,
                        direccion = direccion,
                        m2_terreno = m2_terreno,
                        numero_estacionamientos = numero_estacionamientos)
            
        inm.id_user_id = current_user.id
        inm.save()
        return HttpResponseRedirect('/dashboard/')
    else:
        u_form = InmuebleForm()
    
    return render(request, 'new_inmueble.html',{'u_form': u_form})

@login_required
def inmuebles_update(request):
    id_inmueble = request.GET['id_inmueble']
    if request.method == 'POST':
        inmueble = Inmueble.objects.filter(id=id_inmueble)[0]
        u_form = InmueblesUpdateForm(request.POST, instance=inmueble)
        if u_form.is_valid():
            u_form.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        inmueble = Inmueble.objects.filter(id=id_inmueble).first()
        u_form = InmueblesUpdateForm(instance=inmueble)
    
    context={'u_form': u_form}
    
    return render(request, 'update_inmueble.html', context)     
        
        
@login_required
def eliminar_inmueble(request):
    #Inmueble.objects.get(id=id_inmueble).delete()
    id_inmueble = request.GET['id_inmueble']
    print(id_inmueble)
    if request.method == 'GET':
         inmueble = Inmueble.objects.filter(id=id_inmueble)
         inmueble.delete()    
    return HttpResponseRedirect('/dashboard/')

def acerca(request):
    return render(request,'about.html',{})

@login_required
def bienvenido(request):
    #private_flans = Flan.objects.filter(is_private=True)
    return render(request,'welcome.html',{
        #'private_flans': private_flans
    })
    
def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        
        if form.is_valid():
            
            contact_form = Contactform.objects.create(**form.cleaned_data)
            
            return HttpResponseRedirect('/exito')
    else:
        form = ContactformForm()
            
    return render(request,'contacto.html',{'form' :form})

def exito(request):
    return render(request,'success.html',{})