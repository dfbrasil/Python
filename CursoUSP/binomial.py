def fat(x):

    fat = 1

    while x>=2:
        fat = (fat)*(x)
        x = x - 1

    return fat

n = int(input("Digite o valor da variável n!: "))
k = int(input("Digite o valor da variável k!: "))

if k<=n:
    print(fat(n)/((fat(k)*(fat(n-k)))))
else:
    print("Valores inválidos, não representa um binômio de Newton!!")
