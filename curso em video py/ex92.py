from datetime import datetime
clt = {}
clt['nome'] = str(input('Qual o seu nome? '))
ano = int(input('Ano de nascimento:'))
nct = int(input('Carteira de trabralho (0 = a não tenho): '))
clt['idade'] = datetime.now().year - ano
if nct > 0:
    clt['ctps'] = nct
    clt['contratação']= int(input('Ano de contratação: '))
    clt['salario'] = float(input('Salário: '))
else:
    clt['ctps']= 'Não tem carteira de trabalho'
print('-='*30)
for i, n in clt.items():
    print(f'{i} : {n}')

