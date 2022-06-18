
n = int(input("Digite a quantidade de alunos: "))
i=1
notas=[]

for i in range(n):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
    i = i + 1


t=len(notas)
print("As notas dos",t,"alunos foram:",notas)
print()

soma = 0

i = 0
for i in range(n):
    soma = soma + notas[i]
    i= i + 1

media = soma/t
mediaArred = round(media,2)
print(f"A média dos",t,"alunos foi de: ", mediaArred)
