
l = int(input("Digite a largura do retângulo: "))
h = int(input("Digite a altura do retângulo: "))

auxL = 1
auxH = 1


while auxH <= h:
    while auxL <= l:
        print ("#", end="")
        auxL = auxL + 1
    print ("")
    auxH = auxH + 1
    auxL = 1
