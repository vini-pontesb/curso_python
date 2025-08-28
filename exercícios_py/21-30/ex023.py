num = (input('Digite um número de 0 a 9999 = '))

print('A unidade desse número será {}\nA dezena desse número será {}\nA centena desse número será {}\nO milhar desse número será {}\n'
      .format(' '.join(num).split()[0], ' '.join(num).split()[1], ' '.join(num).split()[2], ' '.join(num).split()[3]))
