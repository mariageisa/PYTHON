#faça um programa que receba a idade de pessoas, até q o valor -1 seja informado
#O programa deve calcular e mostrar a quantidade de pessoas em cada faixa etária e a maior idade. 

#variveis iniciais
n = 1
idade_maior = 0

# disgraça do while
while n > 0:

    #variavel com input para receber a idade
    idade = int(input("Digite sua idade:"))

    #incremento para a condição  se repetir
    n += 1
    #verifica se o valor digitado é -1
    if(idade == -1):    
        print(f'A maior idade é: {idade_maior}') #mostra a idade maior
        break #para o loop do while
    
    #verifica se a idade digitada é maior que a idade anterior digitada
    if(idade > idade_maior):
        idade_mario = idade

    #verifica a faixa etária 1
    if(idade <= 15):
        print("Até 15 anos, faixa etária 1")
    
    #verifica a faixa etária 2
    elif(idade >= 16 and idade <= 40):
        print("Faixa etária 2")
    
    #verifica a faixa etária 3
    elif(idade >= 41 and idade <= 60):
        print("Faixa etária 3")

    #verifica a faixa etária 4
    else:
        print("Faixa etária 4")
        
#FINALIZA O CÓDIGO COM ESTILO
#MARIA GEISA (0.50cm)
