n = float(input('digite 1 número: '))
n2 = float(input('digite outro: '))
n3 = float(input('Digite outro: '))
m = n
if n2<n and n2<n3:
  m = n2
if n3<n and n3<n2:
   m = n3
print('O menor é o : {}'.format(m))

ma = n
if n2>n and n2>n3:
   ma = n2
if n3>n2 and n3>n:
      ma = n3
print(' O maior é o: {} '.format(ma))      