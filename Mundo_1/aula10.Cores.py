'''Cores no pytho
padrão de comando: \033[0;33;44m
style: 0 - none, 1 - Bold, 4 - Underline e 7 - Negative ( Inversão )
Text: 30 à 37
Background: 40 à 47'''

#print('\033[4;31;43mOlá, mundo!\033[m')

nome = 'J. Bezerra'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'preto&branco':'\033[7:30m'}
print('Prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
print('Prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))