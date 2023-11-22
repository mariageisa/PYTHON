# contador = 0
# while contador < 10:
# #Enquanto o contador for menor ou igual a 10 faça:
#     nota = float(input('informe sua nota:  '))
#     if nota < 0 or nota >10:
#         print('Sua nota nãofoi suficiente')
#         break
#     contador = contador + 1

# Peça a idae de 20 alunos. faça um código que avisa quando o aluno tem mais de 13 anos

aluno = 1 
while aluno <= 20:
    idade = int(input(f'Qual idade do aluno {aluno} '))
    if idade > 13:
        print(f'A idade do aluno {aluno} é {idade}. é maior que 13')
    aluno = aluno + 1
print('Fim da questão 1')