# lista  = ['barroso','Marques',18]
# data = int(input('qual ano você nasceu? '))
# datam = str(input('qual mes você nasceu? '))
# datad = int(input('qual dia você nasceu? '))
# nome = str(input('qual é o seu primeiro nome? '))
# unome = str(input('qual é o seu ultimo nome? '))
# lista.insert(2,unome)
# lista.insert(0,nome)
# lista.append(datad)
# lista.append(datam)
# lista.append(data)
# print(lista)

LISTA = []
for c in range(0,5):
    LISTA.append(int(input('digite um valor: ')))

for c,v in enumerate(LISTA):
    print(f'Na posição {c} eu encontrei - {v}')
print('Fim da lista')

# a = [3,6,7,8,4]
# b = a[:]
# b[4] = 5
# print(f'a= {a}')
# print(f'b = {b}')