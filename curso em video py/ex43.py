p = float(input('Qual é o seu peso?:  '))
a = float(input('Qual é a sua altura?: '))
imc =  p/(a*a)
print('Seu imc é: {:.2f}'.format(imc))
if imc<18.5:
 print('Você está abixo do peso ideal')
elif imc>= 18.5 and imc<25:
 print('Você está no peso ideal')
elif imc>=25 and imc<30:
 print('Você está em sobre peso')
elif imc>=30 and imc<40:
 print('Você está obeso')
else:
 print('Você está em obesidade mórbida')