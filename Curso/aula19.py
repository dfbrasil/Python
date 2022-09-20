from audioop import mul


n1 = 10
n2 = 7

def somar():
    r = n1 + n2
    print('Soma de ' + str(n1) +  ' é ' + str(n2) + '=' + str(r))

def subtrair():
    r = n1 - n2
    print('Subratcao de ' + str(n1) +  ' é ' + str(n2) + '=' + str(r))

def multiplicar():
    r = n1 * n2
    print('multiplicação de ' + str(n1) +  ' é ' + str(n2) + '=' + str(r))


def calculos():
    somar()
    subtrair()
    multiplicar()

calculos()
