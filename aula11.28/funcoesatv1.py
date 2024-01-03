# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro. 

'''Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721'''

def inverter_numero(numero):
    numero_invertido = int(str(numero)[::-1])
    return numero_invertido

numero = int(input("Digite um número inteiro: "))
resultado = inverter_numero(numero)
print(resultado)
