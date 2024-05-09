
def ajuda(com):
    print(f'\033[32m{help(com)}')


def titulo(msg,cor=0):
    tam =len(msg)+4

    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)

comando = ''
while True:
    titulo('\033[0;30;42mSISTEM DE AJUDA pyHELP\033[m')
    comando = str(input('\033[0;30;47mFunção ou Biblioteca >\033[m '))
    if comando.upper()== 'FIM':
        break
    else:
        ajuda(comando)
titulo('Fim do Programa')