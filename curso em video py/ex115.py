
from ex115B import arquivoExiste,leraquivo,cadastrar
def cadastro():
    arq = 'cursoemvideo.txt'
    if arquivoExiste(arq):
        print('Arquivo encontrado.')
    else:
        print('Arquivo não encontrado.')

    while True:
        print('-'*30)
        print('\033[1;33mMENU PRINCIPAL\033[m'.center(37))
        print('-'*30,'\033[36m')
        print(1,'- Ver pessoas cadastradas')
        print(2,'- Cadastrar nova pessoa')
        print(3,'- Sair do sistema\033[m')
        print('-'*30,)
        while True:
            
            try:
                n = int(input('Sua opção: '))    
            except (TypeError,ValueError):
                print('\033[31mDigite uma opção entre as 3\033[m')
                continue
            if n>3:
                print('\033[31mDigite uma opção entre as 3\033[m')
                continue
            else:
                break  
        if n ==2:
            print('-'*30)
            print('\033[1;33mCADASTRO\033[m'.center(37))
            print('-'*30)
            no = str(input('Nome: '))
            while True:
                try:
                    id = int(input('Idade: '))
                except (TypeError,ValueError): 
                    print('\033[31mERRO! Digite a idade da forma correta.\033[m')
                    continue
                else:
                    cadastrar(arq,no,id)
                    break
        if n ==1:
            print('-'*30)
            print('\033[1;33mLISTA\033[m'.center(37))
            print('-'*30)
            print(f'\033[1;36m{'NOMES':10} {'IDADES':>5}\033[m')
            leraquivo(arq)
        if n == 3:
            print('FIM, volte sempre')
            break

