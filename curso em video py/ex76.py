valores = ('Caneta' , 2.0, 'Caderno', 10.50, 'Estojo', 5.50, 'Mesa', 200.0, 'Mochila', 59.99, 'Borracha', 1.99)
print("--"*20)
print(f'{"Lista de valores":^40}')
print("--"*20)
for pos in range(0,len(valores)):
    if pos %2==0:
        print(f'{valores[pos]:.<30}', end= '')
    else:
        print(f'R$ {valores[pos]}')              
print("--"*20)
