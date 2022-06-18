
mylist=[]
par=0
impar=0

while True:
    # some code here
    n = float(input("Digite um item da lista:"))
    mylist.append(n)


    if input('Gostaria de inserir um novo intem na lista? ') != 'y':
        tamanho = len(mylist)

        for i in mylist:
            if i%2==0:
                par=par+1
            else:
                impar = impar + 1
        print(par,"Números pares")
        print(impar,"Números ímpares")
        break
