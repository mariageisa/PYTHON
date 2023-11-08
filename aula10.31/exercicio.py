# Escreva um programa que leia a distancia em km e a quantidade1 de litros de combustível consumidos por um carro em um percurso qualquer. Calcule o consumpo em km/l e escreva uma mensagem de acordo com a relação abaixo:

km = int(input('quantos km de distância percorreu (ex:15km)? '))
l = float(input('quantos litros de combustivel estavam disponíveis (ex:)? '))


if (km /l < 8) :
    print("venda o carro")  
if (km /l>= 8) and (km /l <= 14) :   
    print('Econômico')
if  (km / l > 14):
    print('super economico')