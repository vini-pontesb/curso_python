num = int(input("Insira um número para que seja convertido: "))
conversao = int(input(
    "Insira para qual base quer converter através dos números a seguir:\n1 - Binário\n2 - octal\n3 - hexadecimal\nEscolha:"))
if conversao != 1 and conversao != 2 and conversao != 3:
    print("Os valores inseridos devem ser apenas os listados!")
elif conversao == 1:
    print(bin(num))
elif conversao == 2:
    print(oct(num))
elif conversao == 3:
    print(hex(num))
