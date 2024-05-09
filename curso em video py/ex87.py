
todos = [[],[],[]]
par = []
cont = 0 

for i in range(0,3):
    n= todos[0].append(int(input(f'Digite um número para [0,{i}]')))

for i in range(0,3):
    n= todos[1].append(int(input(f'Digite um número para [1,{i}]')))

for i in range(0,3):
    n= todos[2].append(int(input(f'Digite um número para [2,{i}]')))
    
print(f'0:[  {todos[0] [0]:^5}  ] [  {todos[0] [1]:^5}  ] [  {todos[0] [2]:^5}  ] ')
print(f'1:[  {todos[1] [0]:^5}  ] [  {todos[1] [1]:^5}  ] [  {todos[1] [2]:^5}  ] ')
print(f'2:[  {todos[2] [0]:^5}  ] [  {todos[2] [1]:^5}  ] [  {todos[2] [2]:^5}  ] ')


print(f'A soma dos itens da tereceira coluna é:{todos[0][2]+todos[1][2]+todos[2][2]}')
print(f'O maior valor da segunda linha é: {max(todos[1])}')

for i in todos[0]:
    if i % 2 ==0:
        par.append(i)
for i in todos[1]:
    if i % 2 ==0:
        par.append(i)
for i in todos[2]:
    if i % 2 ==0:
        par.append(i)
print(f'A soma dos valores pares é: {sum(par)}')
        
