pessoas = []
nome = []
peso = []
SN = ''
pesado =  leve =  0
while SN != 'N':
    nome.append(str(input('Nome: ')))
    nome.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        pesado = leve = nome[1]
    else:
        if nome[1]>pesado:
            mai = nome[1]
        if nome[1]< leve:
            leve = nome[1]
    pessoas.append(nome[:])
    nome.clear()
    SN = (str(input('Quer continuar? [S/N]'))).upper()[0]
print('+-'*20)
print(f'Temos {len(pessoas)} pessoas cadastradas')
print(f'As pessoas ou pessoa mais pesada com {pesado}KG foram: ', end= ' ')
for p in pessoas:
    if p[1] == pesado:
        print(f'{p[0]}')

print(f'As pessoas ou pessoa mais leve com {leve}KG foram: ',end='')
for p in pessoas:
    if p[1]== leve:
        print(f'{p[0]}',end= ' ')
        

