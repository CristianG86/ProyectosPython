import random

def lanzar_moneda():
    moneda = random.choice(["Cara", "Cruz"])
    return moneda

def probar_suerte(suerte,lista):
    if suerte == 'cara':
        print("La lista se autodestruirá")
        for num in lista:
            (num)
        return lista
    elif suerte == 'cruz':
        print("La lista fue salvada")
        print(lista)
    return lista

suerte = lanzar_moneda()
print(suerte)
lista_numeros = [1,2,3,4,5]
print(probar_suerte(suerte,lista_numeros))