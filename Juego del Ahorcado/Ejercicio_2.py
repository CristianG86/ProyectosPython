def convertir_a_lista(palabra):
    lista_palabra = []
    for indice,n in enumerate(palabra):
        if n not in lista_palabra:
            lista_palabra.append(n)
    lista_palabra.sort()
    print(lista_palabra)

texto = "cristian"
convertir_a_lista(texto)