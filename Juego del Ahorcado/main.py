frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(2,"naranja")
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)

def invertir_palabra(palabra):
    return palabra[::-1].upper()
palabra= "python"
print(invertir_palabra(palabra))

def todos_positivos(lista_numeros):
    retorno = True
    negativos = 0
    positivos = 0
    for n in lista_numeros:
        if n > 0:
            positivos +=1
        elif n < 0:
            negativos +=1
    if negativos > 0:
        retorno = False
    return retorno

lista_numeros = [1,-5,4,3]
print(todos_positivos(lista_numeros))


def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n in range(0,1001):
            suma += n
    return suma
lista_numeros = [1,5,8000,450]
print(suma_menores(lista_numeros))



