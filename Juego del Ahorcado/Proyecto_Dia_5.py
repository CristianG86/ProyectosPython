import random

def elegir_palabra(lista):
    return random.choice(lista)

def convertir_palabra_secreta(palabra):
    palabra_guiones = []
    for letra in palabra:
        palabra_guiones.append("_")
    return palabra_guiones


def pedir_letra():
    letra = input("Elija una letra: ")
    return letra.upper()

def validar_letra(letra):
     if letra.isalpha() == True and len(letra) == 1:
        return letra
     else:
        print("EL caracter ingresado es incorrecto.")

def chequear_letra(letra,lista_letras,lista_oculta):
    indice = 0
    lista_incorrectas = []
    for n in lista_letras:
        if n == letra:
            lista_oculta[indice] = letra
            print(lista_oculta)
        indice += 1
    else:
        lista_incorrectas.append(letra)
        print("Incorrecto")
    print(lista_oculta)
    print(lista_incorrectas)


print("¡Vamos a Jugar al AHORCADO!")
lista_palabras =['manzana', 'naranja','frutilla','sandia']

palabra_secreta = elegir_palabra(lista_palabras)
palabra_secreta = list(palabra_secreta)
print(palabra_secreta)
palabra_oculta = convertir_palabra_secreta(palabra_secreta)
print(palabra_oculta)
print("")
vidas = 6
bandera = False
while vidas != 0 or bandera != True:
    letra_ingresada = pedir_letra()
    validar_letra(letra_ingresada)
    chequear_letra(letra_ingresada,palabra_secreta,palabra_oculta)
    vidas -=1