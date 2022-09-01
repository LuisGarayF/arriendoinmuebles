from m7_python.models import Inmueble

'''CRUD'''

# READ

# Leer todos los inmuebles
def get_all_inmuebles():
    Inm = Inmueble.objects.all()
    return Inm
    
def insertar_inmuebles(lista):    
    id_user = lista[0]
    id_tipo_inmueble = lista[1]
    id_comuna = lista[2]
    id_region = lista[3]
    nombre_inmueble = lista[4]
    descripcion = lista[5]
    m2_construido = lista[6]
    m2_terreno = lista[7]
    numero_estacionamientos = lista[8]
    numero_banios = lista[9]
    numero_habitaciones = lista[10]
    direccion = lista[11]
    
    inm = Inmueble(
        id_user = id_user,
        id_tipo_inmueble = id_tipo_inmueble,
        id_comuna = id_comuna,
        id_region = id_region,
        nombre_inmueble = nombre_inmueble,
        descripcion = descripcion,
        m2_construido = m2_construido,
        m2_terreno = m2_terreno,
        numero_estacionamientos = numero_estacionamientos,
        numero_banios = numero_banios,
        numero_habitaciones = numero_habitaciones,
        direccion = direccion 
    )
    
    inm.save()
    return insertar_inmuebles

# UPDATE

# Actualizar descripcion del inmueble
def actualizar_desc_inmueble(id_inmueble, new_desc):
    Inmueble.objects.filter(pk=id_inmueble).update(descripcion=new_desc)

# DELETE

# Eliminar inmueble

def eliminar_inmueble(id_inmueble):
    Inmueble.objects.get(id=id_inmueble).delete() # Lo mismo sería:  inm = Inmuebles.objects.get(id=id_inmueble) luego un salto de linea :  inm.delete()