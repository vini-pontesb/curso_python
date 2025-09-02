preco = float(input("Insira o valor do produto: "))
condicao = int(input("Qual é a forma de pagamento? \n1 - À vista no dinheiro ou cheque \n2 - Cartão à vista \n3 - Duas vezez no cartão \n4 - Três ou mais vezes no cartão \n: "))
if condicao == 1:
    preco_novo = preco - preco*0.1
    print(f"O preço final é: R$ {preco_novo}")
elif condicao == 2:
    preco_novo = preco - preco*0.05
    print(f"O preço final é: R$ {preco_novo}")
elif condicao == 3:
    print(f"O preço final é: R$ {preco}")
elif condicao >= 4:
    preco_novo = preco + preco*0.2
    print(f"O preço final é: R$ {preco_novo}")
