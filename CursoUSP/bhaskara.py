import math

a = float(input("Primeiramente insira o valor da variável A. "))
print()

b = float(input("Primeiramente insira o valor da variável B. "))
print()

c = float(input("Primeiramente insira o valor da variável C. "))
print()

delta = ((b**2)-(4*a*c))
if delta < 0:
    print ("esta equação não possui raízes reais")

elif delta == 0:
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    print (f"a raíz desta equação é {r1:.2f}")
else:
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)
    if r1 > r2:
        print (f"as raízes da equação são {r2:.2f} e {r1:.2f}")
    else:
        print (f"as raízes da equação são {r1:.2f} e {r2:.2f}")
