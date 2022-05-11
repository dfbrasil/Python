

lista = []
listaInversa= []
n = int(input("Digite um número a ser adicionado a lista: "))

while n != 0:
    lista.append(n)
    n = int(input("Digite um número a ser adicionado a lista: "))

i = len(lista)
print(i)
while i>0:
    listaInversa.append(lista[i-1])
    i = i - 1
print(lista)
print(listaInversa)