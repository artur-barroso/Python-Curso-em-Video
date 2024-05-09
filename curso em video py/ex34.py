s = float(input('\033[1;33mdigite seu salario:\033[m \033[1;31m \033[m'))
c1 = s*15/100
c2 =s*10/100
if s>=1250:
    print('\033[1;mO seu salario agora é {} {} {} reias'.format('\033[1;32m', s + c2, '\033[m'))
else:
    print('Seu salario agora é {} {} {} reias'.format('\033[1;32m' ,s + c1, '\033[m'))