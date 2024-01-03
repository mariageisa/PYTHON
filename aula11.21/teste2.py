
# Inicializar as variáveis
menor_valor = float('inf')# abreviação para infinito
maior_valor = float('-inf')
soma_valores = 0

# Entrada do número inicial
numero = float(input("Digite um número (ou 'q' para sair): "))

# Loop while para receber os números até que 'q' seja digitado
while numero != 'q':
    numero = float(numero)
    
    # Atualizar o menor valor, o maior valor e a soma dos valores
    if numero < menor_valor:
        menor_valor = numero
        
    if numero > maior_valor:
        maior_valor = numero
        
    soma_valores += numero
    
    # Entrada do próximo número
    numero = input("Digite outro número (ou 'q' para sair): ")

# Imprimir os resultados
print("Menor valor:", menor_valor)
print("Maior valor:", maior_valor)
print("Soma dos valores:", soma_valores)