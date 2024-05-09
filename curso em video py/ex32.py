f = int(input('Dige um ano qualquer: '))
if f % 4 == 0 and f %100 !=0 or f % 400 == 0:
    print('{} é bissexto'.format(f))
else:
    print('{} não é bissexto'.format(f))