def buscarAlumno(alumnos:dict, rut:str):
    if rut in alumnos.keys():
        return alumnos[rut]
    else:
        return None
    
#solo de prueba 
#alumnos={'123': {'nombre': 'wacoldo', 'apellido': 'soto', 'asignatura': 'Estructura', 'notas': []}}
#print(buscarAlumno(alumnos,'456'))