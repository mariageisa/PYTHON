#Faça um programa que pede 3 números inteiros. Calcule imprima: - o produto do dobro do primeiro com metade do segundo somado com o terceiro. A soma do triplo do primeiro com o terceiro e multiplicado pelo segundo.

a = input('digite um numero inteiro')
b = input('digite um numero inteiro')
c = input('digite um numero inteiro')

calculo1= ((int(a)*2)* (int(b)/2)+ int(c))
calculo2= ((int(a)*3+ int(c))*int(b))

print (int(calculo1))
print (int(calculo2))