from random import choice
from time import sleep
print('\033[;33mVamos jogar pedra, papel e tesoura?')
print('Vamos ver se consegue me ganhar?\033[m')
sleep(0.5)
p = input('\033[;33mEscolha pedra, papel ou tesoura:\033[m').upper()
l = ['PEDRA', 'PAPEL','TESOURA']
f = choice(l)
print('\033[1;33mQUEM VAI VENCER?..\033[m')
sleep(1.5)
if f=='PEDRA' and p=='PAPEL':
    print('\033[1;32mEu coloquei pedra.Você VENCEU!!!\033[m')

elif f=='PAPEL' and p=='TESOURA':
    print('\033[1;32mEu coloquei papel.Você VENCEU!!!\033[m')

elif f=='TESOURA'and p=='PEDRA':
    print('\033[1;32mEu coloquei tesoura.Você VENCEU!!!\033[m')

elif f=='PEDRA'and p=='TESOURA':
    print('\033[1;31mEu coloquei pedra.Você PERDEU!!!\033[m')

elif f=='TESOURA'and p=='PAPEL':
    print('\033[1;31mEu coloquei tesoura.Você PERDEU!!!\033[m')

elif f=='PAPEL'and p=='PEDRA':
    print('\033[1;31mEu coloquei papel.Você PERDEU!!!\033[m')

else:
    print('\033[1;33mNos 2 escolhemos {}. EMPATE \033[m'.format(f))






