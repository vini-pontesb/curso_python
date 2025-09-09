n = int(input("Insira um número positivo para verificar se ele é primo: "))
tot = 0
for c in range(1, n+1):
    if n%c == 0:
        tot += 1
if tot <= 2 and n>0:
    print(f"O número {n} é primo")
elif tot > 2:
    print(f"O número {n} não é primo")