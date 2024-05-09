n=float(input('Qual a largura da sua parede? '))
n1=float(input('Qual a altura da sua parede? '))
s=n*n1/2
b=s/2
print('Você vai precisar de {:.3f} litros de tinta\nCompre {:.3f} latas de tinta de 2 litros'.format(s, b))