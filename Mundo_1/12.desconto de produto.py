p = float(input('Qual é o preço do produto? R$ '))
d = (5/100) * p
print('O preço que custava R${}, na promoção com desconto de 5% custará R${:.2f}.'.format(p, (p-d)))
