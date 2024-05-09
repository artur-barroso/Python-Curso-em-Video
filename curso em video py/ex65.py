f = n = media = so = maior = menor = 0
while n != 'N':
    f = float(input('digite um número:'))
    media = media + 1
    so = so + f
    if so == 1:
        maior = menor = f
    else:
        if f > maior:
            maior = f
        elif f< menor:
            menor = f 
    n = str(input('quer continuar? [S/N]')).upper().strip()
print('A media desses números é: {:.1f}\nO maior número é: {}\nO menor é: {}' .format(so/media,maior, menor)) 

