homens = mulheres = pessoas =  0
while True: 
 idade = int(input('Qual a idade dessa pessoa? '))

 sexo = str(input('Qual é o sexo dessa pessoa? [F/M]')).upper()[0]
 while sexo not in 'FM':
    sexo = str(input('Qual é o sexo dessa pessoa? [F/M]')).upper()[0]
 
 continuar = str(input('Quer continuar? [S/N] ')).upper()[0] 
 while continuar not in 'SN':
    continuar = str(input('Quer continuar? [S/N] ')).upper()[0] 
 if idade >= 18 :
    pessoas += 1

 if sexo == 'M':
    homens +=1

 if sexo == 'F' and idade < 20:
    mulheres+= 1

 if continuar == 'N':
    break
 
print(f'Esse programa tem {homens} homens \n{pessoas} pessoas maiores de 18 anos \n{mulheres} mulheres menores de 20 anos ')