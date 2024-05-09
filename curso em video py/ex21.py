def calcular_fatorial(numero):
    if numero < 0:
        return "O fatorial de números negativos não está definido."
    elif numero == 0:
        return 1
    else:
        resultado = 1
        contador = 1
        while contador <= numero:
            resultado *= contador
            contador += 1
        return resultado

# Solicitar entrada do usuário
numero = int(input("Digite um número para calcular o fatorial: "))

# Calcular e imprimir o fatorial
resultado_fatorial = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {resultado_fatorial}")