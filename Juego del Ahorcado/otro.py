import random

def elegir_palabra(lista):
    return random.choice(lista)

def convertir_palabra_secreta(palabra):
    palabra_guiones = []
    for letra in palabra:
        palabra_guiones.append("_")
    return palabra_guiones

print("¡Vamos a Jugar al AHORCADO!")
lista_palabras =['manzana', 'naranja','frutilla','sandia']

palabra_secreta = elegir_palabra(lista_palabras)
palabra_secreta = list(palabra_secreta)

palabra_oculta = convertir_palabra_secreta(palabra_secreta)
print(palabra_oculta)