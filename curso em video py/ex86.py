
todos = [[],[],[]]
for i in range(0,3):
    todos[0].append(int(input(f'Digite um número para [0,{i}]')))

for i in range(0,3):
    todos[1].append(int(input(f'Digite um número para [1,{i}]')))

for i in range(0,3):
    todos[2].append(int(input(f'Digite um número para [2,{i}]')))

print(f'0:[  {todos[0] [0]:^5}  ] [  {todos[0] [1]:^5}  ] [  {todos[0] [2]:^5}  ] ')
print(f'1:[  {todos[1] [0]:^5}  ] [  {todos[1] [1]:^5}  ] [  {todos[1] [2]:^5}  ] ')
print(f'2:[  {todos[2] [0]:^5}  ] [  {todos[2] [1]:^5}  ] [  {todos[2] [2]:^5}  ] ')
