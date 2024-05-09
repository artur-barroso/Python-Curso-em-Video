from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
print('_'*10,'<VALORES SORTEADOS>','_'*10 )
for s in range(0,4):
    jogadores[f'jogador {s+1}'] = randint(1,6)
for i, n in jogadores.items():
    print(f'{i} : {n}')
    sleep(1)
ranking = []
ranking = sorted(jogadores.items(),key=itemgetter(1), reverse=True)
for i,r in enumerate(ranking):
    print(f'No {i+1}° lugar ficou o: {r[0]} com {r[1]}')
    sleep(1)

