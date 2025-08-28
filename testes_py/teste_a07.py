n1 = int(input('Fale um valor = '))
n2 = int(input('Fale outro = '))
m = n1 * n2
d = n1 / n2
s = n1 + n2
su = n1 - n2
di = n1 // n2
r = n1 % n2
print('A multiplicação desses valores é {} e a divisão {:.2f}'.format(m, d))
print('A soma desses valores é {} e a subtração é {}'.format(s, su))
print('A divisão inteira desses valores é {} e o resto é {}'.format(di, r))
