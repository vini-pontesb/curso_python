valor_casa = float(input("Insira o valor da sua casa: "))
valor_salario = float(input("Insira o valor do seu salário: "))
anos = int(input("Insira em quantos anos pretende parcelar: "))
prest_anual = valor_casa/anos
prest_mensal = prest_anual/12
if prest_mensal > valor_salario*0.3:
    print("Você não pode fazer este financiamento!")
else:
    print(f"A prestação será R$ {prest_mensal:.2f}")