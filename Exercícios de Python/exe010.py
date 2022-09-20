from datetime import date

data = date.today()

valor = float(input('Digite o valor em Reais: '))
dolar = float(input('Digite o valor de $1 dólar'))

print(f'R${valor} reais no dia {data} equivalem a ${valor/dolar:.2f} dólares.')