v = float(input('digite um valor: '))
v1 = float(input('digite outro valor: '))
v2 = 0
while v2 != 5:
 v2= int(input('[1] soma \n[2] multiplique \n[3] maior  \n[4] novos \n[5] fim \nQual opção escolhe?'))
 if v2 == 1:
  print(' {}+{} =  {}'.format(v,v1,v+v1))
 elif v2 == 2:
  print('{} x {} = {} '.format(v,v1,v*v1))
 elif v2 == 3:
  if v>v1:
   print('o maior número é {}'.format(v))
  else:
   print('O maior número é {}'.format(v1))
 elif v2 == 4:
  v = float(input('digite um valor: '))
  v1 = float(input('digite outro valor: '))
print('fim do programa')

