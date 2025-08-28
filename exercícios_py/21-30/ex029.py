vel = float(input('A quantos KMh o carro passou pelo radar? '))
multa = (vel - 80)*7
if vel <=80:
    print('O carro não foi multado')
else:
    print('Você levou uma multa de R${:.2f}'.format(multa))