n = int(input("Digite um número: "))
i = 0
fat = 1
auxN = n

if n == 0 or n == 1:
    print("1")

else:
    while n!=0:
        fat = fat * (n)
        n = n-1

    print(fat)
