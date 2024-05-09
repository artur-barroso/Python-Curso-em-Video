ma = 0
me = 0
for l in range(1,6):
    i = float(input('peso da {}` pessoa: '.format(l)))
    if l == 1:
        ma = i
        me = i
    else:
        if i> ma:
            ma = i
        if i<me:
            me = i
print('O maior peso lido foi de {}kg e o menor de {}kg'.format(ma,me))