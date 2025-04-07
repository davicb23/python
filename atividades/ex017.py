from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input("Comprimento do ccateto adjacente: "))
h = hypot(co, ca)
print('O valor da hipotenusa é: {:.2f}'.format (h))

'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {}' .format(h))
'''