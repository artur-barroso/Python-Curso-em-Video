exp =(str(input('Digite uma expressão: ')))
lista = []

for simb in exp:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
    else:
        lista.append(')')
        
if len(lista)==0:
    print('Espressão válida')
else:
    print('Expressão invalida')
