import math

print("Esse programa calcula as raízes de uma equação do segundo grau.")
print()

a = input("Primeiramente insira o valor da variável A. ")
print()
a1 = a.isnumeric()
b = input("Primeiramente insira o valor da variável B. ")
print()
b1 = b.isnumeric()
c = input("Primeiramente insira o valor da variável C. ")
print()
c1 = a.isnumeric()

if a1 == True and b1 == True and c1 == True:
    aNum = float(a)
    bNum = float(b)
    cNum = float(c)

    if (aNum != 0 and bNum != 0 and cNum != 0):
        delta = ((bNum**2)-(4*aNum*cNum))

        if delta < 0:
            print ("Essa equação de segundo grau não possui raízes reais")

        elif delta == 0:
            r1 = (-bNum + math.sqrt(delta)) / (2 * aNum)
            print (f"Essa equação de segundo grau possui raízes iguais de valor {r1:.2f}")

        else:
            r1 = (-bNum + math.sqrt(delta)) / (2 * aNum)
            r2 = (-bNum - math.sqrt(delta)) / (2 * aNum)
            print (f"Essa equação de segundo grau possui raízes de valores R1={r1:.2f} e R2={r2:.2f}")

    elif (aNum != 0 and bNum == 0 and cNum != 0):
        r1 = math.sqrt(cNum/aNum)
        r2 = (-1) * math.sqrt(cNum/aNum)
        print(f"Essa equação de segundo grau possui raízes de valores R1={r1:.2} e R2={r2:.2f}")

    elif (aNum != 0 and bNum != 0 and cNum == 0):
        r1 = 0
        r2 = (-bNum/aNum)
        print (f"Essa equação de segundo grau possui raízes de valores R1={r1:.2f} e R2={r2:.2f}")

    elif (aNum == 0 and bNum != 0 and cNum != 0):
        r1 = -cNum/bNum
        print (f"Essa equação é do primeiro grau e possui raíz de valor R={r1:.2}")

    elif (aNum != 0 and bNum == 0 and cNum == 0):
        print ("Essa equação de segundo grau possui raízes iguais de valor R1 = R2 = 0")


else:
    print("Reinicie o programa inserindo números")
