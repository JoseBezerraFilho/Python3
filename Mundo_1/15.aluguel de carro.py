dias = int(input('Quantos dias de aluguel do carro? '))
km = float(input('Quantos kilômetros percorridos? '))
pago = (dias * 60) + (km * 0.15)
print('O aluguel do carro por {} dia(s) e {}km rodados custará R${:.2f}.'.format(dias, km, pago))


