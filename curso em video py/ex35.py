t = float(input('\033[4mDigite quantos cm tem uma reta: '))
t1 = float(input('Digite outro valor: '))
t2 = float(input('Digite outro valor maior que os outros dois: \033[m'))
if t + t1 > t2 and t1 + t2> t and t + t2> t1:
    print('\033[1;32mEssas retas podem formar um triangulo')
else:
    print('\033[1;31mEssas retas não podem formar um triangulo') 