# teste = []
# teste.append('lucas')
# teste.append(40)
# galera = []
# galera.append(teste[:])
# teste[0]= 'Giulia'
# teste[1]= 22
# galera.append(teste[:])
# print(galera)

# galera=[['Artur',18],['Ana',33],['Joaquim',13],['Maria',45]]
# for p in galera:
#     print(f'\033[32m{p[0]}\033[m tem \033[36m{p[1]}\033[m anos de idade.')

galera = []
dado= []
maior = menor = 0
for c in range(0,3):
    dado.append(str(input('Qual é o seu nome?')))
    dado.append(int(input('Qauntos anos você tem?')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1]>= 21:
        print(f'{p[0]} é maior de idade')
        maior+=1
    else:
        print(f'{p[0]} é menor de idade')
        menor+=1
print(f'Temos {maior} maiores  e {menor}  menores de idade')