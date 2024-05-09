# while True:
#  try:
#   f =int(input('\033[37mDigite um número:  '))
#   break
#  except ValueError:
#   print('\033[31mIsso não é um número inteiro\033[m')
  

# try: 
#  f =int(input('DIGITE UM VALOR para ser dividio:'))
#  print('O resultado é: {}'.format(100/f ))
# except ZeroDivisionError:
#  print('Não tem como dividir por zero meu cria') 

class salario:
    def __init__(self, base, bonus):
     self.base = base
     self.bonus = bonus
    def salario_anual(self):    
       return(self.base*12)+self.bonus
    

class empregado:
   def __init__(self, nome, idade, salario):
      self.nome= nome
      self.idade = idade
      self.salario_empregado = salario
   def salario_total(self):
     return self.salario_empregado.salario_anual()
salario = salario(10000, 700)
emp = empregado('musashi', 46, salario)
print(emp.salario_empregado)
      


