
def reducir_lista(lista):
    lista.sort()
    lista.pop(-1)
    lista = set(lista)
    lista = list(lista)
    return lista


def promedio_lista(lista):
    n = 0
    suma = 0
    for num in lista:
        suma +=num
        n +=1
    promedio = suma/n
    return promedio

mi_lista = [1,8,3,9,23,3,2]
reducir_lista(mi_lista)
print(promedio_lista(mi_lista))
print(mi_lista)