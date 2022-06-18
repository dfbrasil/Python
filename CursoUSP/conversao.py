totalsegs = input("Qual a quantidade de segundos que gostaria de converter? ")

qtdhoras = int(totalsegs) // 3600
segundosrestantes = int(totalsegs) % 3600
minutos = segundosrestantes // 60
segundos = segundosrestantes % 60

print (qtdhoras)
print(minutos)
print (segundos)
