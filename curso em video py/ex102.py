def fatorial(n,show=False):
    """
    Calculando o fatorial de um número
    n = O número a ser calculado
    show= Quer mostrar o calculo sim ou não
    return = retorna o valor do fatirial de n
    """
    f = 1 
    for c in range(n,0,-1):
        if show:
            print(c,end=' ')
            if c > 1:
                 print(' x ',end=' ')
            else:
                print(' = ',end=' ')
        f*=c
    return f
print(fatorial(5,True))
help(fatorial)




