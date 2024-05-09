t = float(input('digite o primeiro termo:'))
r= float(input('digite a razão: '))
td = t
d = t
s = 0
print('os 10 primeiros termos são:')
while s<10: 
     print('{:.0f} - '.format(t),end='')
     t+=r
     s+= 1
print('FIM')
     