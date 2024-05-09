from random import randint
def sorteia(lista):
    """
    lista serve para nada mesmo
    """

    print('Sorteando 5 números...')
    for cont in range(0,5):
        nu = randint(1,10)
        lista.append(nu)
        print(nu,end=' ')
    print('\nPronto')

def somapar(lista):
    soma=0
    for valor in lista:
        if valor%2==0:
            soma+=valor
    print(f'Os valores pares são {lista} é {soma}')

numeros = list()
sorteia(numeros)
somapar(numeros)
 

help(sorteia)