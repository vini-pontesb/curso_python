frase = 'Curso em vídeo de python'
# FATIAMENTO DE STRINGS
print(frase[9])
print(frase[0:5])
print(frase[9:24])
print(frase[18:])
print(frase[0:13:2])
print(frase[6::3])
len(frase)
# ANÁLISE DE STRINGS
print(frase.count('o')) # quantos 'o' tem na frase
print(frase.count('o', 0, 13))  # quantos 'o' tem na frase entre 0 e 12
print(frase.find('deo'))  # achar 'deo' em frase
print(frase.find('Android'))
print('Curso' in frase)
# TRANSFORMAÇÃO DE STRINGS
frase = frase.replace('Curso', '  Aula')# troca uma palavra por outra('antiga', 'nova')
print(frase.upper())  # coloca todas as letras em maiúsculo
print(frase.lower())  # coloca todas as letras em minúsculo
print(frase.capitalize())  # coloca todas as letras em minúsculo, menos a primeira
print(frase.title())  # coloca todas as primeiras letras, após um espaço, em maiúsculo
print(frase.strip())  # retira todos os espaços vazios na frase (no início ou fim)
print(frase.rstrip())  # retira todos os espaços vazios do lado direito na frase
print(frase.rstrip())  # retira todos os espaços vazios do lado direito na frase
print(frase.lstrip())  # retira todos os espaços vazios do lado esquerdo na frase
# DIVISÃO DE STRINGS
print(frase.split())  # transforma cada palavra, separada por um espaço,em uma string
# JUNÇÃO DE STRINGS
print(' '.join(frase))# junta as palvras colocando o que estiver no '' entre elas
