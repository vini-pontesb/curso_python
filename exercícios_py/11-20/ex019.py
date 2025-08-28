import random
al1 = input('Digite seu nome: ')
al2 = input('Digite seu nome: ')
al3 = input('Digite seu nome: ')
al4 = input('Digite seu nome: ')
name_list = [al1, al2, al3, al4]
escolhido = random.choice(name_list) #choice serce para sorte apenas um nome na lista
print('O aluno escolhido foi {}'.format(escolhido))
