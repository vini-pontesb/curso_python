for a in range(0, 6, 2): #conta de 1 a 6, pulando duas casas
    print(a)
print("___________________________\n")
n = int(input("Insira um número inteiro maior que 1: ")) #conta de n a 1, pulando menos uma casa
for b in range(n, 0, -1):
    print(b)
print("___________________________\n") #conta de i a f pulando p casas
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for c in range(i, f+1, p):
    print(c)