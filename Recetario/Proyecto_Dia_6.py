from os import system
import os
from pathlib import Path
import shutil

def cantidad_recetas(guia):
    cont = 0
    for txt in Path(guia).glob("**/*.txt"):
        cont +=1
    return cont

def elegir_categoria(guia):
    print("")
    print("Las categorías son:")
    print("")
    for carpeta in os.listdir(guia):
        print(carpeta)
    print("")
    categoria_elegida = input("Ingrese la categoría elegida: ")
    return categoria_elegida

def mostrar_recetas(guia,categoria):
    directorio = Path(guia,categoria)
    print("")
    for txt in os.listdir(directorio):
        print(Path(txt).stem)
    print("")
    ver_receta = input("¿Qué receta desea ver?: ")
    print("")
    print(Path(guia,categoria,ver_receta + ".txt").read_text())
    print("")
    elegir = input("¿Desea ver otra receta? S/N: ").upper()
    print("")
    if elegir == "S":
        categoria2 = elegir_categoria(guia)
        mostrar_recetas(guia,categoria2)

def crear_receta(guia, categoria):
    nombre_receta = input("Ingrese el nombre de la receta: ")+".txt"
    ruta_nueva = Path(guia, categoria, nombre_receta)
    receta_nueva = open(ruta_nueva,"x")
    receta_nueva.write(input("Ingrese la receta: "))

def crear_categoria(guia):
    print("Las categorías son:")
    print("")
    for carpeta in os.listdir(guia):
        print(carpeta)
    nombre_categoria = input("Ingrese el nombre de la categoría: ")
    os.makedirs(Path(guia, nombre_categoria))

def eliminar_archivo(guia,categoria):
    directorio = Path(guia, categoria)
    print("")
    for txt in os.listdir(directorio):
        print(Path(txt).stem)
    print("")
    eliminar_receta = input("¿Qué receta desea eliminar?: ")
    Path(directorio,eliminar_receta + ".txt").unlink()

def eliminar_categoria(guia, categoria):
    directorio = Path(guia,categoria)
    shutil.rmtree(directorio)



opcion = 0
while opcion != 6:
    print("¡BIENVENIDOS AL RECETARIO!")
    ruta = Path(Path.home(), "Desktop\Recetas")
    print(f"Las recetas se encuentran guardadas en: {ruta}")
    print(f"La cantidad de recetas guardadas es: {cantidad_recetas(ruta)}")
    print("-------MENÚ -------")
    print("1. Mostrar una receta.")
    print("2. Crear receta.")
    print("3. Crear categoría.")
    print("4. Eliminar receta.")
    print("5. Eliminar categoría.")
    print("6. Salir")
    print("")
    opcion = int(input("Ingrese la opcion deseada: "))
    if opcion == 1:
        categoria = elegir_categoria(ruta)
        mostrar_recetas(ruta,categoria)
    elif opcion == 2:
        categoria = elegir_categoria(ruta)
        crear_receta(ruta,categoria)
    elif opcion == 3:
        crear_categoria(ruta)
    elif opcion == 4:
        categoria = elegir_categoria(ruta)
        eliminar_archivo(ruta,categoria)
    elif opcion == 5:
        categoria = elegir_categoria(ruta)
        eliminar_categoria(ruta,categoria)


    system("cls")
print("¡Gracias, vuelve pronto!")





