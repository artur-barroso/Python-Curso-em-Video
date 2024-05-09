n = soma = conta = 0 
while True:
    n = int(input('digete um número [digite 999 para parar]:  '))
    if n == 999:
        break
    soma = soma + 1
    conta += n
print(f'você digitou {soma} números e a soma entre eles é {conta}')
  