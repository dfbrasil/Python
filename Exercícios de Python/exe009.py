n = int(input('Digite um número pra ver sua tabuada: '))
cont = 0
print('-' * 12)
while (cont<=10):
    print(f'{n} x {cont:2} = {n*cont}')
    cont+=1
print('-' * 12)