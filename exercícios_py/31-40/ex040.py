nota1 = float(input("Insira sua primeira nota: "))
nota2 = float(input("Insira sua segunda nota: "))
media = (nota1 + nota2)/2
if media < 5:
    print(f"Sua média foi {media} e você está reprovado")
if 5 <= media <= 6.9:
    print(f"Sua média foi {media} e você está de recuperação")
elif media >= 7:
    print(f"Sua média foi {media} e você está aprovado")
