import os

# Se le indica al archivo donde estan las rutas de la config de Django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

from m7_python.models import Inmueble, Region, Comuna


def get_list_inmuebles(name,descr):
    lista_inmuebles = Inmueble.objects.filter(nombre_inmueble__contains=name).filter(descripcion__contains=descr)
    
    with open('inmuebles.txt','a') as f:
        for l in lista_inmuebles.values():
            #print(str(l))
            f.write(str(l))
            f.write('\n')
            
    return lista_inmuebles

#get_list_inmuebles('Casa','arriendo')


def get_lista_inmuebles_by_comuna(comuna):
    """Consulta a la base de datos sin utilizar ORM Django"""
    select = f"""
    SELECT A.id, A.nombre_inmueble, A.descripcion, B.region, C.comuna
    FROM public.m7_python_inmueble as A
    INNER JOIN public.m7_python_region as B
    ON A.id_region_id = B.id 
    INNER JOIN public.m7_python_comuna as C
    ON A.id_comuna_id = C.id
    WHERE C.comuna LIKE '%%{str(comuna)}%%'    
    """
    results = Inmueble.objects.raw(select)
    
    with open('li_comuna.txt','a') as a:
        for p in results:
           a.write(p.nombre_inmueble+','+p.descripcion)
           a.write('\n')

    return results

#get_lista_inmuebles_by_comuna('Bernardo')

def get_lista_inmuebles_by_region(id):
    """Obtener lista de inmuebles por region"""
    region = str(Region.objects.filter(id=id).values()[0]["region"])
    
    lista_inmuebles = Inmueble.objects.filter(id_region_id=id)
    
    with open('li_region_orm.txt','a') as r:
        for p in lista_inmuebles.values(): 
           r.write(str(str(p['nombre_inmueble'])))
           r.write(',')
           r.write(region)
           r.write('\n')

#get_lista_inmuebles_by_region(16)    


# Lo mismo que el anterior pero directamente con el nombre de la region y haciendo la consulta sin el ORM de Django
def get_list_inmuebles_by_region(region):
    """Consulta a la base de datos sin utilizar ORM Django"""
    select = f"""
    SELECT A.id, A.nombre_inmueble, A.descripcion, B.region, C.comuna
    FROM public.m7_python_inmueble as A
    INNER JOIN public.m7_python_region as B
    ON A.id_region_id = B.id 
    INNER JOIN public.m7_python_comuna as C
    ON A.id_comuna_id = C.id
    WHERE B.region LIKE '%%{str(region)}%%'    
    """
    results = Inmueble.objects.raw(select)
    
    with open('li_region.txt','a') as a:
        for p in results:
            a.writelines('*' * 50)
            a.writelines('*' * 5 + " Lista de inmuebles por Region " + '*' * 5)
            a.writelines(f'-'*50) 
            a.writelines(f'\n \t Nombre|\t\t Descripción\n')
            a.writelines(f'\n \t{p.nombre_inmueble}|\t\t{p.descripcion} \n')
            a.writelines('*' * 50) 
           
#get_list_inmuebles_by_region("Metro")

