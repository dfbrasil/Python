totalSegundos = int(input("Por favor, entre com o número de segundos que deseja converter:"))

totalDias = totalSegundos // 86400
restoSegundosDia = totalSegundos % 86400
horas=restoSegundosDia//3600
minutos = (restoSegundosDia - (horas*3600))//60
segundos = (restoSegundosDia - (horas*3600) - (minutos*60))


print (totalDias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
