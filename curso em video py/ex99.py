print('~~'*30)

def maior(*v):
    print('Analisando...')
    print(f'Os valores foram {v} ao todo {len(v)} valores')
    h= max(v)
    print(f'O maior valor é {h}')
    print('~~'*30)
    if maior == ():
        print('Não tem número maior')
    
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0) 