def remove_repetidos():

    lista = []
    lista2 = []
    listaFinal = []
    n = 1

    while True:
        n = int(input("Digite um numero:"))
        if n >= 0:
            lista.append(n)
        else:
            break

    i = 0

    for i in range(len(lista)):
        valor = lista[i]
        listaCLone = lista[:]
        lista2 = listaCLone[0:i]
        if valor not in lista2:
            listaFinal.append(valor)

    listaFinal.sort()
    print(listaFinal)


remove_repetidos()
