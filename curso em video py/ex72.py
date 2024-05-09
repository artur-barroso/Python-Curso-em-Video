números = ('zero', 'um', 'dois','tres', 'quatro', 'cinco','seis', 
'sete', 'oito', 'nove', 'dez','onze', 'doze', 'treze','quatorze', 'quinze',
'dezesseis','dezessete', 'dezoito', 'dezenove', 'vinte')

valor = int(input('digite um número de 1 a 20: '))
while valor > 20 or valor < 0:
    valor = int(input('digite um número de 1 a 20: '))

print(f'Você digitou o número {valor[números]}')   
