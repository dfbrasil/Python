

n = int(input("Digite um número: "))
n1 = n
resto = 0
soma = 0
próximo = 0

while n > 0:

    resto = n%10
    n = n//10

    soma = soma + resto

print ("A soma dos digitos de",n1,"é",soma)
