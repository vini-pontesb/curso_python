from datetime import datetime


def alistamento(ano_nasc):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nasc
    if idade < 18:
        print("Você ainda irá se alistar!")
    if idade == 18:
        print("Está na hora de se alistar!")
    if idade > 18:
        print("Já passou do seu tempo de alistamento!")


ano_nascimento = int(input("Insira seu ano de nascimento: "))
alistamento(ano_nascimento)
