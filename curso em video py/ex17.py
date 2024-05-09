from math import sqrt
co = float(input('cateto oposto: '))
ca = float(input('cateto adjacente: '))
h1 = (co ** 2 + ca ** 2) 
h2= sqrt(h1)
print(' a hipotenusa vai medir: {:.2f} '. format(h2))