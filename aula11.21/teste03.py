'''Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
 Um número primo é aquele que é divisível somente por ele mesmo e por 1'''
#variavel que irá recolher o numero
numero = int(input('Digite um numero inteiro: '))
contador = 0
#trabalho com intervalo, o +1 é para ir até o numero
intervalo =range(1, numero+1)
for i in intervalo: 
    if numero % i == 0:
        print(f'foi divisivel por {i}')
        contador += 1
if contador == 2 or numero == 1:
        print(f'o numero {numero} é primo')
 