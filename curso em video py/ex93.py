jogador = {}
gol = []
jogador['nome'] = str(input('Qual o nome do jogador? '))
partidas = int(input('Quantas partidas ele jogou? '))
for i in range(partidas):
    gol.append(int(input(f'Quantos gols na partida {i+1}:')))
    jogador['gols'] = gol
for g in range(partidas):
    print(f' => Na {g+1}° partida: {jogador['nome']} fez {gol[g]}')
print('-='*30)
print(f'No total {jogador['nome']} fez {sum(gol)} gols nos {partidas} jogos')
jogador['total'] = sum(gol)
print('-='*30)
print(jogador)
print('-='*30)
print(f'No campo nome tem o valor : {jogador['nome']}')
print(f'No campo gols tem o valor: {jogador["gols"]}')
print(f'No campo total: tem o valor: {jogador['total']}')
