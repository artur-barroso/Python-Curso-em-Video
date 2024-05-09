f= int(input('digite um número: [dite 999 para parar]:'))
f= 0
cont = f
s = 0 
while f != 999:
    cont= cont + f
    s = s + 1 
    f= int(input('digite um número: [dite 999 para parar]:'))
print(cont, s)    