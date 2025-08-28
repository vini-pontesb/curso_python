num1 = int(input('Digite um número inteiro = '))
num2 = int(input('Digite um número inteiro = '))
num3 = int(input('Digite um número inteiro = '))
if num1 > num2 and num1 > num3:
    print('O primeiro número, {}, é o maior número'.format(num1))
if num1 < num2 and num1 < num3:
    print('O primeiro número, {} é o menor número'.format(num1))

if num2 > num1 and num2 > num3:
    print('O segundo número, {} é o maior número'.format(num2))
if num2 < num1 and num2 < num3:
    print('O segundo número, {} é o menor número'.format(num2))

if num3 > num2 and num3 > num1:
    print('O terceiro número, {} é o maior número'.format(num3))
if num3 < num2 and num3 < num1:
    print('O terceiro número, {} é o menor número'.format(num3))
