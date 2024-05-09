n = 0
soma = 0 
x= 0
while True:
    n = int(input('Quer saber a taboada de qual número?'))
    if n <0:
       break
    for c in range(1,11):
     print(f'{n} x {c} = {n*c}')
print('fim')   