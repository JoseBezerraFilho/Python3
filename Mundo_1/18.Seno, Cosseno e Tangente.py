from math import radians, cos, sin, tan
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
print('O ângulo de {} tem o Seno de {:.2f}.'.format(ang, seno))
cosseno = cos(radians(ang))
print('O ângulo de {} tem o Cosseno de {:.2f}.'.format(ang, cosseno))
tangente = tan(radians(ang))
print('O ângulo de {} tem a Tangente de {:.2f}.'.format(ang, tangente))



