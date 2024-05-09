
f = int(input('digite um valor para a sequencia de fibonacci: '))
s = 0 
print('os {} primeiros valores da sequencia de fibonacci são: '.format(f)) 
t1 = 0
t2 = 1
while s<f:
    print(t2 ,' - ',  end='')
    t3 = t1+t2
    s+=1
    t1 = t2
    t2 = t3
print('fim') 
