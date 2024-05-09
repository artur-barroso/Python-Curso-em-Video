cont = 0 
lista = []
while True:
    numero = lista.append(int(input('Digite um número: ')))
    cont += 1
    SN = str(input('Quer continuar? [S/N]')).upper()
    while SN not in 'SN':
        SN = str(input('Quer continuar? [S/N]')).upper()
    if SN == 'N':
        break
print(f'Você digitou {cont} números')
lista.sort(reverse=True)
print(f'Os números do maior para o menor {lista}')
print(f'O maior valor foi: {max(lista)}')
