velocidade = float(input('Qua é a velocidade do seu carro? '))
if velocidade > 80:
    print('Multado, você excedeu o limite que é de 80km/h!')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança! ')