s = float(input('Qual o salário de um funcionário? R$'))
p = float(input('Qual a porcentagem do aumento? '))
a = (p/100 + 1) * s
print('Um funcionário que ganhava R${:.2f}, com {:.0f}% de aumento, passa a receber R${:.2f}' .format(s, p, a))