gasto = menor = contador = barato = contador = maisbarato =  0 
print('-'*30)
print('cadastro de produtos')
print('-'*30)
while True:
    produto = str(input('qual o nome do produto? '))

    valor = float(input('qual o valor dele? R$'))    

    opção = ' '
    while opção not in 'SN':
        opção = str(input('quer cadrastrar mais algum produto? [S/N]')).upper()[0]

    gasto += valor
    contador+=1

    if contador ==1:
        barato = valor
        maisbarato = produto
    else:
        if valor < barato:
            barato = valor
            maisbarato = produto
    if valor > 1000:
        menor+= 1
    
    if opção =='N':
        break

print(f'Você gastou R${gasto} no total\n{menor} produtos custam mais de R$1000 \nO produto mais barato foi o {maisbarato}') 