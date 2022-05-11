import random

def main():

    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    p = int(input("2 - para jogar um campeonato "))

    if p == 1:
        partida()
    elif p == 2:
        print("**** Rodada 1 ****")
        partida()
        print("**** Rodada 2 ****")
        partida()
        print("**** Rodada 2 ****")
        partida()
        print("**** Final do campeonato! ****")
        print("Placar: Você 0 X 3 Computador")
    else:
        print("Opção inválida!")


#-----------------------------------------------------------
def partida():

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    while True:

        if n < m:
            print("Quantidade limite maior que a quantidade de peças.")
            n = int(input("Quantas peças? "))
            m = int(input("Limite de peças por jogada? "))

        else:
            # n = n
            # m = m
            break

    if n % (m + 1) == 0:
        print ("Você começa!")

    else:
        print("Computador começa!")

    if n % (m + 1) != 0:
        i = 1

    else:
        i = 2

    while n>0:

        if i % 2 != 0:
            pecas = computador_escolhe_jogada(n,m)
            n = n - pecas
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                break

        elif i %2 == 0:
            pecas = usuario_escolhe_jogada (n,m)
            n = n - pecas
            if n == 0:
                print("Fim do jogo! O usuário ganhou!")
                break
        i = i + 1
#-------------------------------------------------------------
def computador_escolhe_jogada(n,m):

    pecas = 1

    if pecas == m:
        print("O computador tirou",pecas,"peça.")
        print ("Agora restam",n - pecas,"peças no tabuleiro.")
        return pecas

    elif n == m:
        pecas = m
        print("O computador tirou",pecas,"peça.")
        print ("Agora restam",n - pecas,"peças no tabuleiro.")
        return pecas

    while pecas != m:
        if (n-pecas) % (m + 1) == 0:
            print("O computador tirou",pecas,"peça.")
            print ("Agora restam",n - pecas,"peças no tabuleiro.")
            return pecas

        else:
            pecas = pecas + 1
            print("O computador tirou",pecas,"peça.")
            print ("Agora restam",n - pecas,"peças no tabuleiro.")
            return pecas

        return pecas

#--------------------------------------------------------------

def usuario_escolhe_jogada (n,m):

    while True:

        pecas = int(input("Quantas peças você vai tirar? "))
        if pecas > m or pecas <= 0 or pecas > n:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            print("Voce tirou",pecas,"peças.")
            print("Agora restam",n-pecas,"peças no tabuleiro.")

            return pecas
#--------------------------------------------------------------


main()
