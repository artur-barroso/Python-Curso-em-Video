n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
n3 = int(input('Digite um número:'))
n4 = int(input('Digite um número:'))
tupla = n1, n2, n3, n4

print(f'O número 9 aparece: {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'o número 3 apareceu pela primeira vez na {1+tupla.index(3)}ª posição')
else:
    print(f'Você não digitou o número 3 ')
print('Os números pares são:')
for pares in tupla:
    if pares %2==0:
       print(pares,end= ' ')


   