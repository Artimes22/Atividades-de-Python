a = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede? '))
area = a*l
tinta = area / 2
print('Para pintar uma parede de {}X{} com {}m² vai ser necessario {}l de tinta'.format(a, l, area, tinta))