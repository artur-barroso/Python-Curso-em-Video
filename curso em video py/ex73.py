times = 'Atlético-MG','Flamengo','Palmeiras',' Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará,Internacional', 'São Paulo', 'Athletico-PR, Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense', 'cruzeiro'
print(f'Os 5 primeiros times são:{times[0:5]}')
print('\033[33m~~\033[m'*50)
print(f'Os times do Z4 são:{times[-4:]}')
print('\033[33m~~\033[m'*50)
print(f'a chapecoense esta na posição: {times.index('Chapecoense')}') 
print('\033[33m~~\033[m'*50)
print(f'Os times em ordem alfabetica:{sorted(times)}')
print('\033[33m~~\033[m'*50)