aluno = input('Qual é o nome do(a) aluno(a)? ')
not1 = int(input('Quanto {} tirou na primeira prova? '.format(aluno)))
not2 = int(input('Quanto {} tirou na segunda prova? '.format(aluno)))
med = (not1 + not2)/2
print('A média do {} foi {:.1f}'.format(aluno, med))
