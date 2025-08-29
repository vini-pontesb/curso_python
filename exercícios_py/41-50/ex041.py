from datetime import datetime


def natacao(ano_nasc):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nasc
    if idade <= 9:
        print("Você está na categoria mirim")
    elif 9 < idade <=14 :
        print("Você está na categoria infantil")
    elif 14 < idade <= 19:
        print("Você está na categoria junior")
    elif 19 < idade <= 20:
        print("Você está na categoria sênior")
    else:
        print("Você está na categoria master")


ano_nascimento = int(input("Insira seu ano de nascimento: "))
natacao(ano_nascimento)
