t = float(input('\033[4mDigite quantos cm tem uma reta: '))
t1 = float(input('Digite outro valor: '))
t2 = float(input('Digite outro valor: \033[m'))
if t + t1 > t2 and t1 + t2> t and t + t2> t1:
    print('\033[1;32mEssas retas podem formar um triangulo\033[m')
    if t ==t1 == t2:
        print('Essas retas formam um triangulo \033[1;33mequilátero \033[m')
    elif t1 == t or t1== t2 or t == t2:
     print('Essas retas formam um triangulo \033[1;33misóceles  \033[m')
    elif t1!=t2 or t1!=t or t!=t2:
     print('Essas reetas forma um triangulo \033[1;33mescaleno \033[m')

else:
    print('\033[1;31mEssas retas não podem formar um triangulo\033[m') 