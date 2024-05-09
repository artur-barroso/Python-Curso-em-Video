ficha = list()
while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    resp=str(input('Quer continuar? [S/N]: ')).upper()
    if resp =='N':
        break
print('fim') 
print(f'{'NO':<4}{'NOME':<10}{"MEDIA":>8}')
print('-'*33)
for i, a in enumerate(ficha):
    if a[2]>=6:
        print(f'{i:<4}{a[0]:<10}\033[32m{a[2]:>8.1f}\033[m')
    else:
        print(f'{i:<4}{a[0]:<10}\033[31m{a[2]:>8.1f}\033[m')
while True:
    opc= int(input('Mostrar notas de qual aluno(999 terminar a pesquisa): '))
    if opc == 999:
        print('-'*15,'FIM','-'*15)
        break
    if opc <= len(ficha) - 1: 
        print(f'Notas de \033[32m{ficha[opc][0]}\033[m são {ficha[opc][1]}')
        print('-'*30)
