# def soma(a,b):
#     s = a+b
#     print(f'A = {a} e B = {b} ',end=' ')
#     print(f'A soma de {a} + {b} = {s}',)

# soma(b=4,a=5) 
# soma(8,9) 

# def contador(*num):
#     print(len(num))

# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

# def dobra(lst):
#     pos = 0
#     while pos< len(lst):
#         lst[pos]*=2
#         pos+=1

# valores = [6,3,9,1,0,2]  
# print(valores)
# dobra(valores)
# print(valores)
 
def soma(*valores):
    s = 0
    for num in valores:
        s+=num
    print(f'Somando os valores {valores} temos {s}')


soma(5,6)
soma(2, 9, 4)
