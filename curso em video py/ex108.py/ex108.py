import uteis


valor = float(input('Digite o preço: '))
print(f'A metade de  {uteis.moeda(valor)} é {uteis.moeda(uteis.dividir(valor))}')
print(f'O dobro é {uteis.moeda(uteis.dobro(valor))}')
print(f'aumentando 10% temos {uteis.moeda(uteis.porcem(valor)+valor)}')
