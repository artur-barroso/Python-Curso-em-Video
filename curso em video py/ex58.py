from random import randint
from time import sleep
s = 1
pc = randint(0,10)
print('\033[36m-+-'*20)
print('\033[37mVou pensar em número entre 0 e 5')
print('\033[36m-+-'*20)
j = int(input('\033[37mTente acertar:'))
print('Carregando...')
sleep(0.5)
while j != pc:
    j = int(input('\033[31mNão é {} tente acertar denovo:\033[m'.format(j)))
    sleep(0.5)
    s = s + 1
print('\033[32mvoce acertou e precisou de {} tentativas'.format(s))    
