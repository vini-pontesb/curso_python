num1 = int(input('Digite um número inteiro = '))
num2 = int(input('Digite um número inteiro = '))
num3 = int(input('Digite um número inteiro = '))
tri1 = num1 + num2
tri2 = num1 + num3
tri3 = num2 + num3
if tri1 < num3 or tri2 < num2 or tri3 < num1:
    print('Essas retas não formam um triângulo') 
else:
    print('Essas retas formam um triângulo')
