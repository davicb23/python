from math import radians, sin, cos, tan

a = float(input('Digite o ângulho que você deseja: ')) 

'''aqui, pra evitar a repitição da chamada do radians, já foi criada logo uma var'''
rad = radians(a)
s = sin(rad)
c = cos(rad) 
t = tan(rad)

'''F strings abaixo, trocar pelo .format, são mais otimizadas'''
print(f'O ângulo de {a}° tem o SENO de {s:.2f}')
print(f'O ângulo de {a}° tem o COSSENO de {c:.2f}')
print(f'O ângulo de {a}° tem a TANGENTE de {t:.2f}')

