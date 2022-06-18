lista = []

while True:
    n = int(input("Digite um numero:"))
    if n != 0:
        lista.append(n)
    else:
        break

t = (len(lista))

while t > 0:
    print(lista[t-1])
    t = t-1
