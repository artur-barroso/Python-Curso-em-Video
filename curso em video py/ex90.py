aluno = {}
aluno['nome'] = str(input('Nome:')).title()
aluno['media']= float(input(f'Media de {aluno['nome']}: '))
print( '-='*15)
print(f'Nome é {aluno['nome']}')
print(f'Média é {aluno['media']}')
if aluno['media'] >= 7:
    aluno['Situação']= '\033[32mAprovado\033[m'

elif aluno['media']<7 and aluno['media']>=5:
    aluno['Situação']= '\033[33mRecuperação\033[m'
else:
    aluno['Situação'] = '\033[31mReprovado\033[m'
print(f'Situação: {aluno['Situação']}')