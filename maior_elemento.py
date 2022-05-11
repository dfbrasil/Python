lista = []


def maior_elemento(lista):
    i = 0
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    print(maior)
    return(maior)
