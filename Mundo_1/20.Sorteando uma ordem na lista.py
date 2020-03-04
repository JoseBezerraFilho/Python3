import random
a = input('Primeiro jogador: ')
b = input('Segundo jogador: ')
c = input('Terceiro jogador: ')
d = input('Quarto jogador: ')
lista = [a, b, c, d]
random.shuffle(lista)
print('A ordem de início do jogo será:')
print(lista)