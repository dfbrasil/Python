l = int(input("Digite a largura do retângulo: "))
h = int(input("Digite a altura do retângulo: "))

auxL = 1
auxH = 1

while auxH <= h:
    while auxL <= l:
        if  auxL == 1 or auxL == l or auxH == 1 or auxH == h:
            print ("#", end="")
            auxL = auxL + 1
        elif auxL != 1 or auxL != l or auxH != 1 or auxH != h:
            print(" ", end="")
            auxL = auxL + 1
    print ("")
    auxH = auxH + 1
    auxL = 1
