from pathlib import Path
import os

def elegir_categoria(guia):
    for carpeta in os.listdir(guia):
        print(carpeta)
    categoria_elegida = input("Ingrese la categoría elegida:")
    return categoria_elegida

def mostrar_recetas(guia,categoria):
    directorio = Path(guia,categoria)
    print(directorio)
    for archivo in os.listdir(directorio):
        print(Path(archivo).stem)

base = Path.home()
print(base)
ruta = Path(base,"Desktop\Recetas")
print(ruta)
cont = 0
for txt in Path(ruta).glob("**/*.txt"):
    cont +=1
print(cont)


categoria = elegir_categoria(ruta)
mostrar_recetas(ruta,categoria)



