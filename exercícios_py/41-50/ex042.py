num1 = int(input('Digite um número inteiro = '))
num2 = int(input('Digite um número inteiro = '))
num3 = int(input('Digite um número inteiro = '))
tri1 = num1 + num2
tri2 = num1 + num3
tri3 = num2 + num3
if tri1 < num3 or tri2 < num2 or tri3 < num1:
    print('Essas retas não formam um triângulo')
elif num1 == num2 == num3:
    print('Essas retas formam um triângulo equilátero')
elif num1 == num2 != num3 or num1 == num3 != num2 or num2 == num3 == num1:
    print('Essas retas formam um triângulo isóceles')
elif num1 != num2 != num3:
    print('Essas retas formam um triângulo escaleno')