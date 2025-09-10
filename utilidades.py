from colorama import Fore
from os import system

def enrojo(texto:str):
    return Fore.RED + texto + Fore.RESET

def pausa():
    input(Fore.LIGHTCYAN_EX + "Presione una tecla para continuar..." + Fore.RESET)
    system("cls")

def validarString(var:str,atributo:str, minimo:int):
    while True:
        
        if len(var)>=minimo:
            break
        print(enrojo(f"Debe ingresar el {atributo}"))
        var=input(f"Ingrese {atributo}:")
    return var