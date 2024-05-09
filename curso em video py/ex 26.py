f = str(input('digite uma frase: ')).strip().upper()
print('Quantas vezes aparece a letra A: {}'.format(f.count('A')))
print( 'em qual posição o A aparece na primeira vez:  {}'.format(f.find('A')+1))
print(' a ultima letra A aparece na posição: {}'.format(f.rfind('A')+1))