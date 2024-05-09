def dividir(n=0,format=False):
    s= n/2
    return s if format is False else moeda(s)

def  dobro(n=0,format=False):
    d = n*2
    return d if format is False else moeda(d)


def porcemais(n=0,tan=0,format=False):
    s= n *tan /100 +n
    return s if format is False else moeda(s)

def porcemenos(n=0,tan=0,format=False):
    s= n - (n *tan /100)
    return s if format is False else moeda(s)


def moeda(preço, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')


def resumo(preço=0,taxa=10,taxar=5):
    print('-'*33)
    print('RESUMO DO VALOR'.center(33))
    print('-'*33)
    print(f'Preço analisado:\t{moeda(preço)}')
    print(f'Dobro de preço: \t{dobro(preço,True)}')
    print(f'Metade do preço: \t{dividir(preço,True)}')
    print(f'Aumentando {taxa}% \t\t{porcemais(preço,taxa,True)}')
    print(f'Diminuindo {taxar}% \t\t{porcemenos(preço,taxar,True)}')
    print('-'*33)

def  leiadinheiro(msg):
    valido = True
    while not valido:
        entrada= str(input(msg))
        if entrada.isalpha():
            print(f'ERRO!:{entrada} não é valido')
        else:
            valido=True
            return float(entrada)


