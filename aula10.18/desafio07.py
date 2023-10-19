#Faça um programa que pede 3 números inteiros. Calcule imprima: - o produto do dobro do primeiro com metade do segundo somado com o terceiro. A soma do triplo do primeiro com o terceiro e multiplicado pelo segundo.

num1= input('digite um numero inteiro')
num2= input('digite um numero inteiro')
num3= input('digite um numero inteiro')

calculo1= ((int(num1)*2)+ (int(num2)/2)+ int(num3))
calculo2= ((int(num1)*3+ int(num3))*int(num2))

print (int(calculo1))
print (int(calculo2))