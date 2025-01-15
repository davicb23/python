# talvez mais pra frente eu aprenda a otimizar mais esse código
v = float(input('Qual o preço do produto? R$'))
d = float(input('Qual o desconto?'))
vcd = (100 - d)/100 * v 
print('O produto que custava R${:.2f}, na promoção com desconto de {:.0f}% vai custar R${:.2f}' .format(v, d, vcd))