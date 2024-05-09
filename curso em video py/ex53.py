f = str(input('digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
inv= ''
for le in range(len(j)-1, -1, -1):
 inv += j[le]
if inv == j:
 print('{} É PALíNDROMO'.format(inv))
else:
 print('Não temos um palíndromo')