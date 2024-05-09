s = str(input('qual o seu sexo? [F/M]')).upper().strip().upper()[0]
while s not in 'MF':
   s = str(input('Responda com [F/M]')).upper()
print('obrigado')