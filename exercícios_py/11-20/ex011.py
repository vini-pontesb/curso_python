h = float(input('Quantos metros tem a altura da parede? '))
l = float(input('Quantos metros tem a largura da parede? '))
a = h*l
tinta = a/2
print('Sabendo que a parede tem {:.1f}m de altura e {:.1f}m de largura, então sua área equivale a {:.1f}m², ou seja, será necessário {:.1f}L de tinta'.format(
    h, l, a, tinta))
