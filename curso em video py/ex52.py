f = int(input('Digite um número e vamos ver se ele é primo: '))
t = 0
for c in range(1,f+1):
    if f % c==0:
        print('\033[32m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ', )       
if t ==2:
    print('\033[33m\n{} é primo'.format(f))
else:
    print('\033[33m\n{} não é primo'.format(f))

