from busqueda import buscarAlumno

def ingresaralumno(alumnos:dict, rut:str, nombre:str, ape:str, asignatura:str):
    try:
        #validar que no exista el rut
        if rut in alumnos:
            raise Exception
        
        
        alumnos[rut]={
            "nombre":nombre,
            "apellido":ape,
            "asignatura":asignatura,
            "notas":[]
        }
        return True,alumnos
    except Exception:
        return False
    
    
def ingresarNota(rut:str,nota:int,alumnos:dict):
    #verficar si existe
    alumno=buscarAlumno(alumnos,rut)
    
    if alumno!=None:
        #agregar la nota
        notas=list(alumno["notas"]) #50,60
        notas.append(nota)
        alumno["notas"]=notas
        
    #respuesta
    return alumnos


#solo de prueba 
#alumnos={'123': {'nombre': 'wacoldo', 'apellido': 'soto', 'asignatura': 'Estructura', 'notas': [50,60]}}
#print(buscarAlumno(alumnos,'456'))

#alumnos=ingresarNota('123',100,alumnos)

#print(alumnos)