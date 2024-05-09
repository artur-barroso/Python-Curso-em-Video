def dividir(n=0):
    s= n/2
    return s

def  dobro(n=0):
    d = n*2
    return d


def porcem(n=0):
    s= n *10 /100
    return s


def moeda(preço, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')