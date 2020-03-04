distancia = float(input('Informe a distância da sua viagem: '))
print('Você está prestes a começar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    passagem = distancia * 0.50
    print('O preço da sua passagem será de R${:.2f}.\nTenha um a ótima viagem.'.format(passagem))
else:
    passagem = distancia * 0.45
    print('O preço da sua passagem será de R${:.2f}. Tenha uma ótima viagem.'.format(passagem))




