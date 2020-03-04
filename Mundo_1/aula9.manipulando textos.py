#Manipulando cadeia de texto
# Técnica do Fatiamento
frase = 'Curso em Video Python'
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# Análise de String
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo')) #começou na posição 11
print(frase.find('android'))#não existe esta string, logo o retorno será -1
print('Curso'in frase)

#Transformação de String
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())# Remove espaços antes e depois da string
print(frase.rstrip())# Remove espaços à direita da string
print(frase.lstrip())# Remove espaços à esquerda da string

# Técnicas de Divisão
print(frase.split())#Divide a string trasnformando numa lista
dividido = frase.split()
print(dividido[0][3])

# Técnica de Junção - inverso do split
print(''.join(frase))