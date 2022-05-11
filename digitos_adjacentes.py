n = int(input("Digite um número: "))
adjacentes = False
naux = n

while n>0:

    aux1 = n%10
    aux2 = n//10
    aux3 = aux2%10
    n = aux2

    if aux1 == aux3:
        adjacentes = True

if adjacentes == True:
    print("sim")
else:
    print("não")
