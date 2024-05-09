nomes = 'Artur', 'Barroso', 'Marques', 'Rosa', 'Julia', 'Liva', 'Gabriel', 'Giulia', 'Biel', 'Tutu', 'Miguel'
print(f'Quias vogais temos nesses nomes?')
for p in nomes:
    print(f'\nEm "\033[34m{p}\033[m" temos', end=' ')
    for l in p:
        if l.lower() in 'aeiou':
            print(f'-{l}',end= '')