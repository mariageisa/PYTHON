
#Peça a idade de 20 alunos. Faça um codigo quando o aluno tem mais de 13 anos 

# contador = 0 

# while contador < 20:
#     idade_aluno = int(input('informe a sua idade: '))
#     if idade_aluno > 13:
#         print(f'o aluno {contador} tem mais de 13 anos')
#     contador += 1

#Faça um código que peça uma nota entre 0 e 10, se a nota for menor que 0 e maior que 10 saia do codigo
while True:
  nota = int(input('informe uma nota: '))
  if nota < 0 or nota > 10:
    break
