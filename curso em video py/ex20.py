import random
n= input('nome primeiro aluno: ')
n2= input('nome segundo  aluno: ')
n3= input('nome terceiro aluno: ')
n4= input('nome quarto aluno: ')
l = [n, n2, n3, n4]
h= random.shuffle(l)
print('o aluno que vai apagar o quadro é o:{}' .format(l))