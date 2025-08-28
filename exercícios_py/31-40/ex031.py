dist = int(input('Qual é a distância, em quilômetros, desta viagem? '))
p200 = 0.5*dist
p201 = 0.45*dist
if dist <=200:
    print('Sua viagem será de R${:.2f}'.format(p200))
else:
    print('Sua viagem será de R${:.2f}'.format(p201))
