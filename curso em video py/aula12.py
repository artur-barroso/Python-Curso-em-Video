n = input('Digite seu nome: ').capitalize()
if n == 'Artur':
 print('Que nome bonito {}'.format(n))
elif n == 'Princesa':
  print('Eu te amo {}{}{}'.format('\033[1;32m' ,n, '\033[m'))
elif n == 'Giulia':
  print('Não é assim que eu te chamo')
else:
  print('Não godtei do seu nome')
print('Bom dia, {}!!'.format(n))