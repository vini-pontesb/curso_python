func = input('Escolha um funcionário pelo seu primeiro e segundo nome = ')
sal = float(input('Qual é o salário, em reais, de {}? '.format(func)))
taxa = sal*1.15
print('Após um aumento de 15% no slário, {} passará a ganhar R${:.2f}'.format(func, taxa))
