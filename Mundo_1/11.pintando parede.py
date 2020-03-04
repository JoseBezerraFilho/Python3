l = float(input('Largura da parede em metros:'))
h = float(input('Altura da parede em metros:'))
area = l * h
tinta = area / 2
print('Para pintar uma parede de dimensões {}m x {}m e de área {}m²'.format(l, h, area))
print('Você precisará de {}l de tinta.'.format(tinta))