def contar_primos(*args):
    cont = 1
    lista_primos = []
    for arg in args:
        for arg:
            if arg % cont == 0:
                cont += 1
        if cont == 2:
            lista_primos.append(arg)
    print(lista_primos)

lista_numeros = [4,5,6,7,8,9,13,15]
contar_primos(lista_numeros)
