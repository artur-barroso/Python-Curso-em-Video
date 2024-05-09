def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
        else:
            return n 
        
def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO! Digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
        else:
            return n 

n = leiaint('Digite um número: ' )
b = leiafloat('Digite um número real: ')
print(f'Você acabou de digitar os números {n} e {b}')
