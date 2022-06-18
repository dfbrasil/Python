while True:

    fat = 1

    n = int(input("Digite um número inteiro positivo. "))
    print()
    aux = n

    if n >= 0:
        while n > 0:

            fat = fat * (n)
            n = n - 1

        print("O fatorial de",aux,"é:", fat)
        print()
    else:
        break
