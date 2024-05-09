def arquivoExiste(nome):
    try:
        a=open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criararquivo(nome):
    try:
        a= open(nome,'wt+', 'r', encoding='utf-8')
        a.close()
    
    except:
        print('ERRO na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado.')
def leraquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('ERRO ao ler o arquivo.')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:10}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq,nome='SEMNOME',idade=0):
    try:
        a= open(arq,'at')
    except:
        print('ERRO.')
    else:
        try:
            a.write(f'{nome};{idade}\n') 
            with open('arquivo.txt', 'r', encoding='utf-8') as f:
                arq = f.read()
        except:
            print('Não conseguimos colocar os dados no arquivo.')
        else:
            print('Informações cadastradas.')
