#Crie um código que receba o salário atual de um funcionário, que receba o valor em porcentagem de reajuste e calcule o valor do novo salário reajustado de acordo com valor de reajuste(%).

atual_salario = float(input("qual seu salario atual?  "))
reajuste_salario = float (input('Qual a porcentagem de reajuste de salario?  '))

novo_salario =  (int(reajuste_salario) * int(atual_salario) /100 + (atual_salario))

print (f'o valor do novo salario com reajuste será de: {novo_salario}')