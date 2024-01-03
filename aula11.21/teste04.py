'''Faça um programa que peça para 10 pessoas a sua idade, ao final o 
programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 a 60 e maior que 60; e então, 
dizer se a turma é jovem ou adulta ou idosa, conforme a média calculada'''


idades=[]
soma= 0
#Pedir a idade de 10 pessoas
for i in range(10):
    idade= int(input('digite a idade da pessoa: '))
    idades.append(idade)
#soma = soma + idade
    soma+= idade 
    
#Calcular a media das idades
media = soma/ len(idades)

#verificar em qual faixa etária a média se encaixa
if  media >= 0 and media <= 25:
        print("turma jovem")
elif media >= 26 and media <=61:
        print("turma adulta")
else:
    print('turma idosa')
