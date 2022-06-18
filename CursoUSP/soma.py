
soma = 0
pergunta = "S"


while pergunta == "S" or pergunta == "s":

    pergunta = (input("Deseja inserir um número na soma? S/N "))

    if pergunta == "S" or pergunta == "s":

        n = int(input("Qual? "))

        soma = soma + n

print(" A soma é", soma)
