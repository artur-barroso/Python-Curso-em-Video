lista = []
listapar = []
listaimpar = []
while True:
    valores = lista.append(int(input('Digite um valor: ')))
    SN = str(input('Quer continuar? [S/N]')).upper()
    while SN not in 'SN':
     SN = str(input('Quer continuar? [S/N]')).upper()
    if SN == 'N':
       break
for c in lista:
    if c %2 == 0:
      listapar.append(c)
    else:
      listaimpar.append(c)
print(f'Você digitou essa lista {lista}\nEsses são os valores pares {listapar}\nEsses são os valores impares da lista {listaimpar}')

      