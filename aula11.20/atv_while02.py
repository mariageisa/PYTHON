#Faça um codigo que leia 5 numeros e informe o maior numero.

maior = 0 
contador = 1

while contador <=5 :
    numero=int(input('digte um numero: '))
    if numero >maior:
     print(numero)
    contador = contador + 1
   
    