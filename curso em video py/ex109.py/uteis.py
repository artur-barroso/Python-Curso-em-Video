def dividir(n=0,format=False):
    s= n/2
    return s if format is False else moeda(s)

def  dobro(n=0,format=False):
    d = n*2
    return d if format is False else moeda(d)


def porcem(n=0,format=False):
    s= n *10 /100 +n
    return s if format is False else moeda(s)


def moeda(preço, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')