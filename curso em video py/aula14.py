# n = 1
# while n != 0 :
#      n = int(input('gitite um valor: '))

# print('fim')    

# r = 'S'
# while r == 'S':
#     n = int(input('digte um valor: '))
#     r = str(input('Quer continuar? [S/N]')).upper()
# print('fim')    

par = impar = 0
n = 1
while n != 0:
    n =int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
         par += 1
        else:
         impar += 1
print('Ai tem {} numeros pares e {} numeros impares'.format(par, impar))    
