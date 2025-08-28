import math
cata = float(input('Qual é o valor, em metros, do cateto adjacente? '))
cato = float(input('Qual é o valor, em metros, do cateto oposto? '))
hip = math.hypot(cata, cato) #hip serve para calcular a hipotenusa
print('Com o cateto adjacente {}m e o cateto oposto {}m, a hipotenusa é {:.2f}m'.format(
    cata, cato, hip))
