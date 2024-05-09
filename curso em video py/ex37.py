num =int(input('Digite um número inteiro: '))
print('''Em qual base quer converter?
    [1] Converter para BINÁRIO
    [2] Converter para OCTAL
    [3] Converter para HEXADECIMAL''')
op = int(input('Sua opção:  '))

if op ==1:
 print('{} em BINÁRIO é: {}'.format(num, bin(num)[2:]))

elif op == 2:
  print('{} em OCTAL é:{}'.format(num, oct(num)[2:]))

elif op == 3:
  print('{} em HEXADECIMAL é:{}'.format(num, hex(num)[2:]))
else:
  print('RESULTADO NÃO ENCOONTRADO')
