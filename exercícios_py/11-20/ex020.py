import random
al1 = input('Digite seu nome: ')
al2 = input('Digite seu nome: ')
al3 = input('Digite seu nome: ')
al4 = input('Digite seu nome: ')
name_list = [al1, al2, al3, al4]
random.shuffle(name_list) #shuffle serve para sortear a ordem da lista
print('A ordem da lista será\n{}'.format(name_list))
