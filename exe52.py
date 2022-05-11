lista = []
i=0
pos1=0
pos2=1

while True:

    quest = input("Deseja iserir um novo item à lista?")

    if quest == "s" or quest == "S":

        novoItem = float(input("Digite um novo intem para a lista"))

        lista.append(novoItem)

    else:

        break
print("A lista é ", lista)

tamLista = len(lista)

while pos2<tamLista:

    if lista[pos1] < lista[pos2]:

        pos1 = pos1 + 1
        pos2 = pos2 + 1

        if pos2 == tamLista:
            print ("crescente")
    else:
            print("não crescente")
            break
