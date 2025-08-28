nome = input('Digite seu nome inteiro = ').strip()
print('O seu nome inteiro é = {}'.format(nome))
print('O seu primeiro nome é = {}'.format(nome.split()[0]))
print('O seu último nome é = {}'.format(nome.split()[len(nome.split())-1]))
