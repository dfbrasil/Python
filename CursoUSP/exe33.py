

n = int(input("Digite um número:"))

prod = 1
i=1

while (prod < n):
    prod = i*(i+1)*(i+2)
    i=i+1

    if (prod==n):
        break

if (prod==n):
    print(n,"É um número triangular.")
else:
    print(n,"Não é um número triangular.")
