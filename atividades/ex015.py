d = int(input('Quantos dias Alugados? '))
km = float(input('Quantos KM rodados? '))
total = (d * 60) + (km * 0.15)
print('Total a pagar é de R${:.2f}' .format(total))