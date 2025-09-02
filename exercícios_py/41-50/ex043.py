# IMC = peso / (altura x altura)
peso = float(input("Insira o seu peso em kg: "))
altura = float(input("Insira a sua aultura em m: "))
IMC = peso/(altura*altura)
if IMC < 18.5:
    print(f" Seu IMC é {IMC:.2f} e você está abaixo do peso")
elif 18.5 <= IMC <= 25:
    print(f" Seu IMC é {IMC:.2f} e você está no peso ideal")
elif 25 <= IMC <= 30:
    print(f" Seu IMC é {IMC:.2f} e você está no estado de sobrepeso")
elif 30 <= IMC <= 40:
    print(f" Seu IMC é {IMC:.2f} e você está no estado de obesidade")
elif IMC > 40:
    print(f" Seu IMC é {IMC:.2f} e você está no estado de obesidade mórbida")