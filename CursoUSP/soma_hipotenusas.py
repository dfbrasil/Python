def calcular_hip(a, b):
    return ((a*a) + (b*b))

def soma_hipotenusas(n):
    c = 1
    soma = 0
    while (c <= n):
        _c = (c*c)       
        a = 1
        b = 1
        while (a < n):
            while (b < n):
                if (_c == calcular_hip(a, b)):
                    #print(a, " - " ,b , " - " , c)
                    soma = soma + c
                    a = n
                    break
                b += 1
            a += 1
            b = a
        c += 1
  
    return soma

print(soma_hipotenusas(25))
