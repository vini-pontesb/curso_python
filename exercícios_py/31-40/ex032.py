ano = int(input('Digite um ano qualquer = '))
bi = ano % 4
if bi == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')
