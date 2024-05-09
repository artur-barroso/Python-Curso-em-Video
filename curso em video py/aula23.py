try:
    a  = int(input('Digite um número:  '))
    b = int(input('Digite um segundo número: '))
    r=a/b
except (ValueError,TypeError):
    print('Tivemos um erro com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero:')
except KeyboardInterrupt:
    print(f'O usuário preferiu não informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Muito obrigado volte sempre.')