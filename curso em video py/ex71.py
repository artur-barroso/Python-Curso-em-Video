print('~-'*20)
print('BANCO BARROSO')
print('~-'*20)
valor = int(input( 'Quanto você quer sacar? R$'))
total = valor
conta = 0
cedula = 50
totcedulas = 0 
while True:
    if total>= cedula:
        total -= cedula
        totcedulas += 1
    else:
        if totcedulas> 0:
            print(f'você vai precisar de {totcedulas} notas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif  cedula == 10:
            cedula = 1
        totcedulas = 0
        if total == 0:
            break
print('volte sempre')      



