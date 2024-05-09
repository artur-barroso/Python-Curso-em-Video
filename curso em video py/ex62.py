t = float(input('digite o primeiro termo:'))
r= float(input('digite a razão: '))
s = 0
tot = 0
m = 9

while m!= 0:
    tot = tot + m
    while s <= tot: 
     print(t)
     t+=r
     s+= 1
    print('ok')
    m = int(input('quantos termos a mais voce quer?'))
print('foram mostrados {} termos '.format(tot))
