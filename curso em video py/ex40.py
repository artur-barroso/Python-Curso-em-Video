p1 = float(input('NOTA DA PRIMEIRA PROVA: '))
p2 = float(input('NOTA DA SEGUNDA PROVA: '))
c = (p1+p2)/2
print('A SUA MEDIA FOI DE {:.1f} PONTOS'.format(c))
if c>= 7:
    print('VOCÊ PASSOU')

elif c> 5.0 and c<= 6.9:
    print('VOCÊ ESTA EM RECUPERAÇÃO')

else:
    print('VOCÊ FOI REPORVADO')