from os import system
from colorama import Fore
from ingresoalumnos import ingresaralumno, ingresarNota
from utilidades import *
from busqueda import buscarAlumno


alumnos={}
#test
alumnos={'123': {'nombre': 'Wacoldo', 'apellido': 'Soto', 'asignatura': 'Estructura', 'notas': [50,70]}}
system("cls")

def datosAlumno(alumno:dict):
    evaluaciones=""
    for nota in alumno["notas"]:
        evaluaciones+=f"{nota} "
        
    if len(alumno["notas"])>0: 
        prom=f"{sum(alumno["notas"])/len(alumno["notas"])}"
    else:
        prom="Sin notas"
    datos=f"""
        NOMBRE: {alumno["nombre"]} {alumno["apellido"]}
        ASIGNATURA: {alumno["asignatura"]}
        NOTAS:{evaluaciones}
        PROMEDIO:{prom}
          """
    
    print(datos)
    
        


def menu():
    print('''
1. Registrar un alumno nuevo
2. Ingresar notas a un alumno existente
3. Mostrar la información completa de un alumno 
4. Mostrar listado de todos los alumnos registrados
5. Mostrar todos los alumnos y el promedio de una asignatura
6. Salir del programa
''')
    
'''PROGRAMA PRINCIPAL'''

while True:
    menu()
    op=input("Ingrese su opción:")
    match op:
        case "1":
            rut=validarString(input("Ingrese rut: "),"rut",3)
            if(buscarAlumno(alumnos,rut)==None):
                nom=validarString(input("Ingrese nombre: "), "nombre", 2)
                ape=validarString(input("Ingrese apellido: "), "apellido", 2)
                asi=validarString(input("Ingrese asignatura: "), "asignatura", 5)
                result=ingresaralumno(alumnos,rut,nom,ape,asi)
                if result!=False:
                    if(result[0]==True):
                        print("Alumno agregado")
                        alumnos=result[1]
                        print(alumnos)
                else:
                    print("Error al agregar alumno")
            else:
                print(enrojo("El rut ya existe!!!!!!"))
                
            
        case "2":
            rut=validarString(input("Ingrese rut: "),"rut",3)
            while True:
                try:
                    nota=int(input("Ingrese nota:"))
                    if 1<nota<100:
                        break
                    else:
                        raise Exception
                    
                except Exception:
                    print("Debe ingresar un valor entre 1 y 100")
            alumnos=ingresarNota(rut,nota,alumnos)
            print(alumnos)
            
            
        case "3":
            rut=validarString(input("Ingrese rut: "),"rut",3)
            alu=buscarAlumno(alumnos,rut)
            
            #MOSTRAR LA INFORMACION DEL ALUMNO
            datosAlumno(alu)
        case "4":
            print("Opción 4")
            #No se donde quedo la ultima version
            
        case "5":
            print("Opción 5")
            
        case "6":
            print("Fin del programa")
            break
        case other:
            print(enrojo("Opción no válida"))
            pausa()
         
        
        
    
    




    
