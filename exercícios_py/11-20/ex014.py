cel = float(input('Informe a temperatura em °C = '))
f = (cel * 9/5) + 32
k = cel + 273.15
print('A temperatura de {}°C equivale a \n{:.1f}F\n{:.1f}K'.format(cel, f, k))
