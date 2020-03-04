salario = float(input('Digite o valor do seu salário: R$ '))
if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 10/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}.'.format(salario, novo))