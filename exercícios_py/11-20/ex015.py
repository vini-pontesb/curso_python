km = float(input('Este carro percorreu quantos KMs? '))
dia = int(input('Quantos dias esse carro foi alugado? '))
vkm = km*0.15
vd = dia*60
vt = vkm + vd
print('Sabendo que o carro rodou {:.1f} KMs e ficou alugado por {} dias, então o valor final do aluguel foi R${:.2f}'.format(
    km, dia, vt))
