# pessoas={'Nome':'Artur','Sexo':'Alfa','Idade':'18'}
# print(f'O nome é :{pessoas['nome']}, ele tem {pessoas['idade']} e seu sexo é {pessoas ['sexo']}')

# print(pessoas.keys()) nome dos valores ex:nome
# print(pessoas.values()) valores ex:Artur
# print(pessoas.items()) tudo
# pessoas['peso']= 73
# del pessoas['Sexo']

# for k,v in pessoas.items():
#     print(f'{k}: {v}')
brasil = list()
estado = dict()
# estado1 = {'uf':'Minas Gerais','Sigla': 'MG'}
# estado2 = {'uf':'São Paulo', 'Sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[0]['Sigla'])
for c in range(0,3):
    estado['uf'] = str(input('Unidade fedetativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v,end=' ')
    print()