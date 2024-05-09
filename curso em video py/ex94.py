pessoas = {}
galera = []
soma = 0
while True:
    pessoas.clear()
    pessoas['nome']= str(input('Nome:'))
    while  True:
        pessoas['sexo']=str(input('Sexo: [F/M]')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO!Responda apenas M ou F')
    pessoas['idade']= int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp= str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-='*15)
print(f'Ao todo temos {len(galera)} pessoas cadrastradas')
media = soma/len(galera)
print(f'A média de idade é de {media:5.2f} anos')
print(f'As mulheres cadastradas são:',end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}',end=' ')
print()
print(f'Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k,v in p.items():
            print(f'{k}= {v}; ',end=' ')
        print()
print('fim')
