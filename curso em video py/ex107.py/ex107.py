import uteis


valor = float(input('Digite o preço: '))
print(f'A metade de R${valor} é R${uteis.dividir(valor)}')
print(f'O dobro é R${uteis.dobro(valor)}')
print(f'aumentando 10% temos R${uteis.porcem(valor)+valor}')
