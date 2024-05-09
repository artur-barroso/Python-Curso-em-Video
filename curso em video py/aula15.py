n = s =  0

while True:
    n = float(input('tente acertar qual número estou pensando: '))
    if  n ==999:
        break
    s +=n
print(f'EU ESTAVA PENSANDO NO NUMERO {n:.0f}. ACERTOU')       