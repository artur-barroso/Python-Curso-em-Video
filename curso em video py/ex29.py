v = float(input('Você estava andando a quanto por hora? '))
c = (v-80)*7
if v >= 80:
    print('você foi multado, pagara 7 reais por cada  km a mais')
    print('pague {} reais pela multa'.format(c))
else:
    print('Tudo certo!!!')

   
