from time import sleep
c =str(input('aperte enter para começar a contagem:'))
for c in range(10,0,-1):
 sleep(1)
 print('\033[1;35m',c , '\033[m')
sleep(1)
print('\033[1;34mFELIZ ANO NOVOOO!!!')