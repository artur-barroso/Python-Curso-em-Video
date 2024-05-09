# ORDEM DE PROCEDENCIA:(), **,(*, /, //, %), (+,-)
# ** == ELEVADO 
# / ==  DIVISÃO
# // == DIVISÃO SEM RESTO
# % == RESTO DA DIVISÃO
 
n1= int(input('digite um valor:'))
n2= int(input('agora outro:'))
s= n1+n2
m= n1-n2
d= n1/n2
e= n1**n2
di=n1//n2
mu=n1*n2
div=n1%n2
 
print('A soma vale: {}\nA subitração: {}\nA divisão: {:.3f}\nA a potencia: {}\nA divisão inteira: {}\nA multiplicasão: {}\nO resto da divisão: {} '.format(s,m, d, e, di, mu, div))