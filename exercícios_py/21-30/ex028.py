import random
n1 = random.randint(0,5)
g = int(input('Digite um numero entre 0 e 5 = '))
if g == n1:
    print('O número escolhido pelo PC foi {}\nParabéns, você acertou!!'.format(n1))
else:
    print('O número escolhido pelo PC foi {}\nQue pena, tente outra vez 😭'.format(n1))
