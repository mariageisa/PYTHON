'''Faça um programa que, dado um conjunto de N números, 
determine o menor valor, o maior valor e a soma dos valores.'''
#RESOLUÇÃO DO PROFRESSOR
maior = 0
menor = None
while True:
    saida = input('Digite "S" para sair: ')
    if saida == 's' or saida == 'S':
       print('Volte sempre!')
       break
    numero = int(input('informe um numero inteiro: '))   

    if numero > maior:
        maior = numero
#O MENOR É NONE = NADA, NEM STR, NEM BOLL, NEM FLOAT: NADA
    if menor == None or numero < menor: 
        menor = numero 
print(f'A soma de {maior} + {menor} = {maior+menor}')
print(f'O maior valor é: { maior }')
print(f'O maior valor é: { menor }')