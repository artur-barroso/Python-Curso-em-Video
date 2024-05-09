from datetime import date
at= date.today().year
tma = 0
tme = 0

for pe in range (1,8,):
    I = int(input('Em que ano  a {}´ pessoa nasceu:'.format(pe)))
    id = at - I
    if id >= 21:
        tma += 1
    else:
        tme+= 1
print('temos {} pessoas maiores de idade e {} menores'.format(tma, tme))



