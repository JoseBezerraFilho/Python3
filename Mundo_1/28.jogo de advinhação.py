from random import randint
from time import sleep
computador = randint(0,5) #Faz o computador 'pensar'
print('-=-' * 20)
print('Vou pensar num número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('em que número eu pensei? '))#jogador tenta advinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns, você consegueu me vencer!')
else:
    print('Ganhei! Pensei no número {} e não no {}!'.format(computador, jogador))

