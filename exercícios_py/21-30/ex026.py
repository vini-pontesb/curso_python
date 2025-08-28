frase = input('Digite uma frase qualquer: ').lower().strip()
print('Nesta frase existe {} letras "a"'.format(frase.count('a')))
print('A primeira letra "a" está na posição {}'.format(frase.find('a')+1))
print('A última letra "a" está na posição {}'.format(frase.rfind('a')+1))
