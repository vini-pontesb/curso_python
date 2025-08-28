nome = str(input('Qual é o seu nome? ')).strip()
# estrutura simples (só com if)
if nome == 'Vinicius': 
    print('Que lindo nome!') 
n1 = int(input('Quanto {} tirou na primeira prova? '.format(nome)))
n2 = int(input('Quanto {} tirou na segunda prova? '.format(nome)))
med = (n1 + n2)/2
# estrutura composta (if e else)
if med >= 6:
    print('{} foi aprovado com {} na média'.format(nome, med ))
else:  
    print('{} foi reprovado com {} na média'.format(nome, med))
