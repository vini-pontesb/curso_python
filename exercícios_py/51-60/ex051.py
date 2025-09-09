n = int(input("Insira um número para começar a PA: "))
r = int(input("Insira a razão: "))
lista = []
for c in range(0, 10):
    lista.append(n)
    n += r
print(lista)