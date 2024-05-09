def voto(n):
    f= 2024-n
    if f > 18 and f<65:
        print(f'Com {f} anos o voto é OBRIGATORIO')
    elif f<18 and f > 15:
        print(f'Com {f} anos o voto é OPICIONAL')
    elif f>=65:
        print(f'Com {f} anos o voto é OPICIONAL')
    else:
        print(f'com {f} anos você NÂO VOTA AINDA')

v = int(input('Em que ano você nasceu?? '))
voto(v) 