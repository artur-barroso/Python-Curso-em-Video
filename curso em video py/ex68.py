from random import randint
print('\033[35m~'*30)
print('Vamos jogar par ou impar?')
print('~'*30)
f = 0
while True:
    pessoa = int(input('\033[33mdigite um número:\033[m'))
    pc = randint(1,10)
    escolha = str(input('\033[33mvocê escolhe impar ou par? [I/P]\033[m')).upper().strip()[0]
    print(f'Eu penssei no número {pc}')
    resultado = pc + pessoa
    print(f'A soma deu {resultado}, ')
    if escolha == 'P':
        if resultado %2 ==0:
            print('\033[32mVocê venceu\033[m')
            f+= 1
        else:
            print('\033[31mVocê peerdeu\033[m') 
            break
    if escolha == 'I':
        if resultado %2 != 0:
            print('\033[32mVocê venceu\033[m') 
            f+= 1
        else:
            print('\033[31mVocê perdeu\033[m')
            break 
    print('\033[33mvamos jogar novamente\033[m') 
print(f'\033[31mGAME OVER!!\033[m. Você venceu \033[32m{f}\033[m vezes')