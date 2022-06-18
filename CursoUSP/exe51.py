notas = []
i=0
recuperacao = 0

while True:

    novaNota = input("Deseja inserir uma nova nota? S/N ")
    print()

    if novaNota == "S" or novaNota == "s":

        nota = float(input("Digite uma nota: "))
        print()

    else:

        qtdNotas = len(notas)
        print("As notas digitadas foram:",notas)
        print()

        for i in range(qtdNotas):
            if notas[i] >=3 and notas[i] < 5:
                recuperacao = recuperacao + 1

        print(recuperacao," Alunos ficaram em recuperação!")

        break

    if nota >= 0 and nota <=10:

        notas.append(nota)
        print()

    else:
        print("Digite uma nota válida!")
        print()
