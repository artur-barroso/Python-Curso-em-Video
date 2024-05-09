from random import randint
from time import sleep
lista= []
jogos = []
print('-='*30)
print('Jogue na mega sena'.center(60))
print('-='*30)
quant = (int(input('Quantos jogos quer fazer?')))
tot =  1 
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num) 
        cont+=1
        if cont>= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print(f'-='*12,'<SORTEANDO>','-='*12)
for i , l in enumerate(jogos):
    print(f'{i+1}° jogo:{l}')
print(f'-='*12,'<BOA SORTE>','-='*12)
