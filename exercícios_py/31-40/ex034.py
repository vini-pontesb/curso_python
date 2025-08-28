sal = float(input('Digite o seu salário = '))
taxa1 = sal*1.10
taxa2 = sal*1.15
if sal > 1250.00:
    print('O seu novo salário será R${:.2f}'.format(taxa1))
else:
    print('O seu novo salário será R${:.2f}'.format(taxa2))
