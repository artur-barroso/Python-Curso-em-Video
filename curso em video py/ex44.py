p = float(input('Qual o valor do produto?: '))
f = str(input('Você vai pagar como:  \na- pix,\nb- cartão de debito, \nc- cartão ate 2x \nd- cartão 3x ou mais \nDigite a letra correspondente: ')).upper()
d = p*10/100
cd = p*5/100
cc = p*20/100
if f=='A':
    print('Você tera 10% de desconto. Você ira pagar {} reais'.format(p-d))
elif f=='B':
    print('Você tera 5% de desconto. Você ira pagar {} reais'.format(p-cd))
elif f=='C':
    print('Você tera 0% de desconto. Você ira pagar {} reias em 2 parcelas de {}reias'.format(p,p/2))

elif f=='D':
  print('Você tera 20% de aumento. Você ira pagar {} reias '.format(p+cc))
C= float(input('vai pagar de quantas vezes: '))
x =p+cc/C
j = x/C
print('Você vai pagar em {} de {}'.format(C,j))


