lista = []
for i in range (0, 6):
    n = int(input("Insira um número: "))
    if n%2 == 0:
        lista.append(n)
soma = sum(lista)
print(soma)