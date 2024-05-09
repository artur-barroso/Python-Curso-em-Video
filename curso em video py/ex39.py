a = int(input('Em que ano você nasceu?  '))
i = 2024-a
print('Você tem por volta de {} anos'.format(i))
if i == 18:
    print('Está na hora de você se alistar')
elif i>18:
    print('Já passou da hora de se alistar.Você já passou {} da idade de alistamento'.format(i-18))
else:
    print('Você ainda não tem idade para se alistar. faltam {} anos para você se alistar'.format(18-i))