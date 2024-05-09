lista = []
lista2= [] 
i = 0
sn = ''
while sn != 'N':
    numero =int(input('Digite um número: '))
    if numero not in lista:
        lista.append(numero)
    else:
        print('esse número ja esta na lista, não vou colocalo novamente')


    sn = str(input('Quer continuar? [S/N]')).upper()
    while sn not in 'NS':
        sn = str(input('Quer continuar? [S/N]')).upper() 
  
    i += 1
print(sorted(lista)) 
