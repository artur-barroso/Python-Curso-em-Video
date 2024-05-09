
lista = []
maior = menor = 0
for i in  range(0,5):
    lista.append(int(input(f'digite um valor na posição {i} : ')))

print(f'Na lista eu encontrei esses valores: {lista}',)
if i == 0:
    maior = menor = lista[i]
else:
    if lista[i]> maior:
        maior = lista[i]
    if lista[i]< menor:
        menor= lista[i]
print(f'O maior valor é {maior} ', end= ' ')  
print(f'O menor valor é {menor}',)            
for i, v in enumerate(lista):
    if v == maior:
        print(f'na posição...{i}...', end= ' ')
    if v == menor:
        print(f'Na posição...{i}...',end= ' ')    
        