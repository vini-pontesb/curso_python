n1 = float(input('Qual foi a sua nota da primeira prova? '))
n2 = float(input('Qual foi a sua nota da segunda prova? '))
med = (n1+n2)/2
cores = {'limpa' : '\033[m',
         'verde' : '\033[32m',
         'vermelho' : '\033[31m'}
if med >= 6:
    print('\033[32mVocê foi aprovado com {} na média!!\033[m'.format(med)) #sem usar o objeto 'cores'
else:
    print('{}Você foi reprovado com {} na média{}'.format(cores['vermelho'], med, cores['limpa'])) # usando o objeto 'cores'