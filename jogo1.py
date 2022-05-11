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

    if n % (m + 1) == 0:
        print ("Você começa!")

    else:
        print("Computador começa!")


    while n>0:
        if n % (m + 1) != 0:
            pecas = computador_escolhe_jogada(n,m)
            n = n - pecas
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                break

        elif n % (m + 1) == 0:
            pecas = usuario_escolhe_jogada (n,m)
            n = n - pecas
            if n == 0:
                print("Fim do jogo! O usuário ganhou!")
                break


#-------------------------------------------------------------

def computador_escolhe_jogada(n,m):

    pecas = 0
    if (n-m) >= m:
        pecas = m - 1
        print("O computador tirou",pecas,"peça.")
        print ("Agora restam",n - pecas,"peças no tabuleiro.")

        return pecas

    elif (n-m)<m:
        pecas = n
        print("O computador tirou",pecas,"peça.")
        print ("Agora restam",n - pecas,"peças no tabuleiro.")

        return pecas

    elif n<=m:
        pecas = n
        print("O computador tirou",pecas,"peça.")
        print ("Agora restam",n - pecas,"peças no tabuleiro.")

        return pecas


#--------------------------------------------------------------

def usuario_escolhe_jogada (n,m):

    pecas = 0
    while True:

        pecas = int(input("Quantas peças você vai tirar? "))
        if pecas > m:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            print("Voce tirou",pecas,"peças.")
            print("Agora restam",n-pecas,"peças no tabuleiro.")

            return pecas
#--------------------------------------------------------------


main()
