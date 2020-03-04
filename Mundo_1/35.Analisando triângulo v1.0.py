print('-='* 20)
print('Analisador De Triângulos')
print('-=' * 20)
a = float(input('Primeiro Segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar umm TRIÂNGULO!')
else:
    print('Os segmentos acima NÃO podem formar um TRIÂNGULO!')
