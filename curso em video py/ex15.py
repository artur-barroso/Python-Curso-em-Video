d = float(input('quantos dias você ficou com o carro?: '))
km = float(input('quantos km você rodou?: '))
c = (60*d) + (0.15*km)
print('Você devera pagar {} reais pelo alugel do carro' .format(c))