lista = []

def soma_elementos(lista):
    i = 0
    soma = 0
    for i in range(len(lista)):
        valor = lista[i]
        soma = soma + valor
    print(soma)
    return(soma)
