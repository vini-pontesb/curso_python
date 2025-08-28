prod = input('Escolha um produto = ')
valor = float(input('Qual é o valor, em reais, do {}? '.format(prod)))
taxa = valor*0.95
print('Após o desconto de 5%, o novo valor do {} é de R${:.2f}'.format(prod, taxa))
