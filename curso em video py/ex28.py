from random import randint
from time import sleep
pc = randint(0,5)
print('\033[36m-+-'*20)
print('\033[37mVou pensar em número entre 0 e 5')
print('\033[36m-+-'*20)
j = int(input('\033[37mTente acertar:'))
print('Carregando...')
sleep(0.5)
if pc == j :
    print('\033[32mVOCÊ ACERTOU!!!!')
else:
    print('\033[31mTente novamente, eu pensei no {}'.format(pc))
