n = int(input("Insira um número inteiro e positivo: "))
t = int(input("Insira até onde a sua tabuada deve multiplicar: "))
for c in range(1, t+1):
    print(f"{n} x {c} = {n*c}")
