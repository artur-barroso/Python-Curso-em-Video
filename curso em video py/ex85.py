
todos = [[],[]]

for i in range(0,7):
    j=int(input(f'Digite {i+1}° número: '))
    if j %2 == 0:
        todos[0].append(j)
    else:
        todos[1].append(j)
todos[1].sort()
todos[0].sort()
# todos.append(par)
# todos.append(impar)
print(f'Os valores pares digitados foram: {todos[0]} ')
print(f'Os valores impares digitados foram: {todos[1]} ')