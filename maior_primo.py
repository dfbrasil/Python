import math

def maior_primo(n):
    cont = 1
    while n>1:

        if n == 2 or n == 3 or n == 5 or n == 7:
            return(n)

        elif n%2==0 or n%3==0 or n%5==0 or n%7==0:
            n = n - 1

        elif (n % math.sqrt(n)) == 0:
            cont = cont + 1
            if cont >=2:
                n = n - 1

        else:
            return (n)
