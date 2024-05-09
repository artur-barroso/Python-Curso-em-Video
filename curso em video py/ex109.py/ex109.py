import uteis


valor = float(input('Digite o preço: '))
print(f'A metade de  {(valor)} é {uteis.dividir(valor,True)}')
print(f'O dobro é {uteis.dobro(valor,True)}')
print(f'aumentando 10% temos {uteis.porcem(valor,True)}')
