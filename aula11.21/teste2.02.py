'''Faça um programa que, dado um conjunto de N números, 
determine o menor valor, o maior valor e a soma dos valores.'''

menor_valor = None
maior_valor = None
soma_valores = 0

# Entrada do número inicial
numero = input("Digite um número (ou 's' para sair): ")

# Loop para receber os números até que 's' seja digitado
while numero != 's' and numero != 'S':
    numero = float(numero)
    
    # Atualizar o menor valor, o maior valor e a soma dos valores
    if menor_valor == None or numero < menor_valor:
        menor_valor = numero
        
    if maior_valor == None or numero > maior_valor:
        maior_valor = numero
        
    soma_valores += numero
    
    # Entrada do próximo número
    numero = input("Digite outro número (ou 'q' para sair): ")

# Verificar se pelo menos um número foi fornecido
if menor_valor is not None:


    print("Menor valor:", menor_valor)
    print("Maior valor:", maior_valor)
    print("Soma dos valores:", soma_valores)
else:
    print("Nenhum número foi fornecido.")