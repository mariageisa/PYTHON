#Escreva uma função chamada gorjeta, que recebe o valor da conta de um restaurante,
# calcule e exibe a gorjeta do garçom, considerando 12% do valor da conta.

'''Faça um programa, com uma função que necessite de um argumento. A função retorna 'P', 
se seu argumento for positivo, e 'N' se for, se seu argumento for zero ou negativo'''

def verificar_sinal(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

argumento = float(input("Digite um número: "))
resultado = verificar_sinal(argumento)
print(resultado)