import math

def Primo(n):

    while n>1:

        if n == 2 or n == 3 or n == 5 or n == 7:
            return(n)

        elif n%2==0 or n%3==0 or n%5==0 or n%7==0:
            n = n - 1

        else:
            k = n
            return(k)
print(Primo(961))

    # if n%2!=0 or n%3!=0 or n%5!=0 or n%7!=0:
    #     return True
    #
    # else:
    #     return False


#escreva uma função éPrimo(k) e faça um laço percorrendo os números até o número dado checando se o número é primo ou não;
# se for, guarde numa variável. Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.
