import random
n= input('nome primeiro aluno: ')
n2= input('nome segundo  aluno: ')
n3= input('nome terceiro aluno: ')
n4= input('nome quarto aluno: ')
l = [n, n2, n3, n4]
h = random.choice (l)
print('o aluno sorteado foi: {} '.format(h))