c = float(input('Qual o valor da casa? '))
s = float(input('Quanto você ganha? '))
a = float(input('Em quantos anos você quer pagar? '))
f = c/(a*12)
print('Sua prestação sera de: {:.2f} reais'.format(f))
if f>= s*30/100:
    print('\033[1;31mVocê não vai dar conta de pagar\033[m')
else:
    print('\033[1;32mSeu financiamento foi aprovado!!!\033[m')
