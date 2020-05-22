import csv
import datetime

#              [ Libreria para validar expreciones regulares ] 
import re

#                      [ Libreria para manejar S.O. ]
import os

#                    [ Se importa las clases de clasePIA ]
from clasePIA import Contacto

#        [ importamos una clase que permite extraer elementos de un objeto ] 
from operator import attrgetter

#        [ Función para mostrar los elementos que tiene la lisa de ejemplo ]
def CuantosElementosHay():
    txt = "El número de elementos de la colección es {}"
    print(txt.format(len(Contactos)))

def BuscarTelefono(telabuscar):
    coincidencia=False
    for contacto in Contactos:
        if (contacto.TELEFONO==telabuscar):
            coincidencia=True
            break
    return coincidencia

def BuscarContacto(telabuscar):
    contador=-1
    indice_retorno=-1
    for contacto in Contactos:
        contador+=1
        if (contacto.TELEFONO==telabuscar):
            indice_retorno=contador
            break
    return indice_retorno

Contactos = []
# Se declara una lista que almacenará objetos. Inicia vacia
CuantosElementosHay()

# Se agregan objetos a la lista.
Contactos.append(Contacto("01MG","Miguel Gonzales","Miguel.Gonzales@unal.edu.mx",6482910463, datetime.date(year=2000,month=9,day=25),1023))
Contactos.append(Contacto("02AL","Ana Laura","Ana.Laura@unal.edu.mx",0923827394, datetime.date(year=2001,month=10,day=30),1222))
CuantosElementosHay()

#Menu

# Se define una función utilizando la expresión lambda, que es equivalente a: os.system('cls')
LimpiarPantalla = lambda: os.system('cls')

# Validador de expresiones regulares
# _txt es el texto a vlidar.
# _regex es el patrón de expresión regular a validar.
def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)

def principal():
    while (True):
        LimpiarPantalla()
        print("LISTA DE COTACTOS")
        print(" ")
        print("[1] Agregar un contacto.")
        print("[2] Buscar un contacto.")
        print("[3] Eliminar un contacto.")
        print("[4] Mostrar contactos.")
        print("[5] Serializar datos.")
        print("[0] Salir.")
        opcion_elegida = input("¿Qué deseas hacer?  > ")
        if RegEx(opcion_elegida,"^[123450]{1}$"):
            if opcion_elegida=="0":
                print("GRACIAS POR UTILIZAR EL PROGRAMA")
                break
            if opcion_elegida=="1":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="2":
                print("Seleccionaste la Opcion Buscar Contacto")
                Telefono=int(input("Ingresa Telefono a Buscar: "))

                indice_obtenido=BuscarContacto(Telefono)
                if indice_obtenido==-1:
                    print("No se encontró el objeto")
                else:
                    print(Contactos[indice_obtenido].TELEFONO)
                    print(Contactos[indice_obtenido].NOMBRE)
                    print(Contactos[indice_obtenido].CORREO)

            if opcion_elegida=="3":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="4":
                print("Mostrando Contactos")
                # Ordenamiento.
                Contactos.sort(key=attrgetter("TELEFONO"),reverse=False)
                # Barrido secuencial.
                for contacto in Contactos:
                    print("------------------------------------------")
                    print(contacto.NICKNAME)
                    print(contacto.NOMBRE)
                    print(contacto.CORREO)
                    print(contacto.TELEFONO)
                    print(contacto.FECHANACIMIENTO)
                    print(contacto.GASTO)
            if opcion_elegida=="5":
                print("Llamar procedimiento para la acción")

            input("Pulsa enter para contunuar...")
        else:
            print("Esa respuesta no es válida.")
            input("Pulsa enter para contunuar...")

principal()
