palavra = input("Insira uma palavra para verificar se ela é palíndrome: ")
palavra_sem_espaco = palavra.replace(" ", "")
tamanho = int(len(palavra_sem_espaco))
a = tamanho-1
z = 0
verificacao = False
for letras in range(0, tamanho):
    x = palavra_sem_espaco[z]
    y = palavra_sem_espaco[a]
    if x == y:
        verificacao = True
    elif x != y:
        verificacao = False
    z += 1
    a -= 1
if verificacao == True:
    print("É palíndromo")
elif verificacao == False:
    print("Não é palíndromo")