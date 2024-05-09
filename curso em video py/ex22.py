f= input('Digite seu nome colpreto: ').strip()
f1 = f.upper()
f2 = f.lower()



print('Seu nome todo maisculo: {}\nSeu nome todo minusculo: {}: '.format(f1,f2, ))
print('O seu nome tem {} letras'.format(len(f)- f.count(' ')))
print('seu primeiro nome tem {} letras'.format(f.find(' ')))