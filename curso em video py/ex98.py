from time import sleep
def contador(i,f,p):
    print('-='*30)
    print(f'Contagem de {i} ate {f} pulando de {p} em {p}')
    if p<0:
        p*=-1
    if p==0:
        p=1

    if i < f:
        cont= 1
        while cont <= f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.1)
            cont+=p

        sleep(1)
    else:
        cont=i
        while cont>=f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.2)
            cont-=p

    print('fim')
    print('-='*30)
contador(1,10,1)
contador(10,0,2)
print('Agora é a sua vez')
ini = int(input('Inicio: '))
fim = int(input('fim: '))
pas = int(input('Passo: '))
contador(ini,fim,pas)