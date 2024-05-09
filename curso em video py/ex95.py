jogador = {}
partidas = []
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Qual o nome do jogador? '))
    tot= int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}:')))
        jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = (input('Quer continuar?? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda com N ou S.')
    if resp == 'N':
        break
print('cod',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print('-='*30)
for k, v in enumerate(time):
    print(f'{k:>4} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-='*30)
while True:
    busca= int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Não existe jogador com esse valor registrado.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i,g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('VOLTE SEMPRE')
