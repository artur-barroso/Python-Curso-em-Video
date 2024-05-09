i = float(input('Quantos anos seu filho tem? '))
if i<=9:
 print('Seu filho esta na categoria MIRIM')
elif i>= 10 and i<=14 :
 print('Seu filho esta na categoria INFANTIL')
elif i>=15 and i<=19:
 print('Seu filho esta na categoria JUNIOR')
elif i>=20 and i<21:
 print('Seu filho esta na categoria SÊNIOR')
else:
 print('Seu filho esta na categoria MASTER')