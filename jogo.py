import random

def main():

    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    p = int(input("2 - para jogar um campeonato "))

    if p == 1:
        while partida()>0:
            partida()

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
            computador_escolhe_jogada(n,m)
            return(n)
        else:
            usuario_escolhe_jogada (n,m)
            return(n)
#-------------------------------------------------------------

def computador_escolhe_jogada(n,m):

    pecasComp = 0
    if (n-m) >= m:
        pecasComp = m - 1
        print("O computador tirou",pecasComp,"peça.")
        print ("Agora restam",n - pecasComp,"peças no tabuleiro.")

        return pecasComp

    else:
        pecasComp = m
        print("O computador tirou",pecasComp,"peça.")
        print ("Agora restam",n - pecasComp,"peças no tabuleiro.")

        return pecasComp

#--------------------------------------------------------------

def usuario_escolhe_jogada (n,m):

    pecasUsuario = 0
    while True:

        pecasUsuario = int(input("Quantas peças você vai tirar? "))
        if pecasUsuario > m:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            print("Voce tirou",pecasUsuario,"peças.")
            print("Agora restam",n-pecasUsuario,"peças no tabuleiro.")

            return pecasUsuario
#--------------------------------------------------------------


main()
