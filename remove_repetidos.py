lista = []
lista2 = []
listaFinal = []


def remove_repetidos(lista):
    i = 0

    for i in range(len(lista)):
        valor = lista[i]
        listaCLone = lista[:]
        lista2 = listaCLone[0:i]
        if valor not in lista2:
            listaFinal.append(valor)

    listaFinal.sort()
    return(listaFinal)
