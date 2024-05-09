from random import randint
cont =  maior = menor =  0 
for cont in range(0,5):
    l = randint(0,10)
    print(l, end = ' ')
    cont += 1
    if cont == 1:
     maior += l
    else:
       if cont> maior:
          maior = l
    if cont == 1:
       menor += l
    else:
       if cont<menor:
          menor =l
print(f'\nO maior valor sorteado foi o: {maior}')  
print(f'O menor valor sorteado foi o: {menor}')       
