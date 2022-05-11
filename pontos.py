import math

x1 = float(input("Digite o valor para X1: "))
y1 = float(input("Digite o valor para Y1: "))
x2 = float(input("Digite o valor para X2: "))
y2 = float(input("Digite o valor para Y2: "))

p = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))

if p>=10:
    print("longe")
else:
    print("perto")
