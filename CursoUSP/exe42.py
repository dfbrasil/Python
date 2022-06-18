
qtdAlunos = int(input("Digite a quantidade de alunos: "))
notas = []
i=0
aprovado = 0
muitobom = 0
reprovado = 0
recuperacao = 0
aluno = 1

for i in range(qtdAlunos):
    print("Digite a nota do",aluno,"º aluno")
    nota = float(input("Digite a nota:"))
    notas.append(nota)
    aluno = aluno + 1

i = 0
for i in range(qtdAlunos):
    if notas[i] >= 3 and notas[i] < 5:
        recuperacao = recuperacao + 1
    elif notas [i] < 3:
        reprovado = reprovado + 1
    elif notas[i] >= 5:
        aprovado = aprovado + 1

i = 0
for i in range(qtdAlunos):
    if notas[i] > 8:
        muitobom = muitobom + 1

print("Quantidade de alunos:",qtdAlunos)
print()
print("As notas dos alunos foram:",notas)
print()
print("A quantidade de alunos reprovados foi de:",reprovado)
print()
print("A quantidade de alunos em recuperação foi de:",recuperacao)
print()
print("A quantidade de alunos aprovados foi de:",aprovado)
print()
print("A quantidade de alunos que obtiveram notas muito boas foi de",muitobom)
