#1 crie uma lista de alunos com nome e nota final de cada aluno e coloque em um dicionario, depois imprima.

# dicionario = {}
# alunos = [['paulo', 5], ['joao', 6], ['fernanda', 8]]
# dicionario.update(alunos)
# alunos_novos = [['ana', 8], ['mika', 10], ['luan', 8], ['iris', 10]]
# dicionario.update(alunos_novos)
# print(dicionario)

# dicionario_ordenado = sorted(dicionario.items())
# print(dicionario_ordenado)

#2 ainda na questão 1 inserir mais 4 alunos e notas no seu dicionário.

#3 faça um codigo que peça a marca e um modelo do carro do cliente insere ele em uma lista e depois transforme em dicionario
#imprima os dois resultados.

'''Aqui virou uma tupla, tornou- se um dado imutavel'''
# marca = input('digite a marca do seu carro: ')
# modelo = input('digite o modelo do seu carro: ')
# lista = [marca, modelo],
# dic = {}
# dic.update(lista)

# print(lista, dic)
'''

lista_carros= []

marca = input('digite a marca do seu carro: ')
modelo = input('digite o modelo do seu carro: ')

lista_carros.append(marca)
lista_carros.append(modelo)

dic_carros = {}
dic_carros.update([lista_carros])

print(lista_carros)
print(dic_carros)'''




#Crie um cadastro de clientes recebendo nome, idade, data de aniversario e endereço(rua, numero da residencia
# e bairro) Adicione todas as informações em um dicionário. imprima o final
# cadastro = []
# cadastro.append(nome)
# cadastro.append(idade)
# cadastro.append(data_de_aniversario)
# cadastro.append(rua)
# cadastro.append(numero_residencia)
# cadastro.append(bairro)

# nome = input('Qual o seu nome? ')
# idade = input('Qual sua idade? ')
# data_de_aniversario = input('Qual a data do seu aniversário? ')
# rua = input('qual o nome da rua onde mora? ')
# numero_residencia = input('Qual o numero da sua residencia?  ')
# bairro = input('Qual o nome do bairro? ')


# dic_cadastro ={
#     "nome": nome,
#     "idade": idade,
#     "data de aniversario": data_de_aniversario,
#     "rua": rua,
#     "numero da residencia": numero_residencia,
#     "Bairro": bairro
# }

# print(dic_cadastro)

#5 vamos criar um sistema de login e senha. crie um dicionário contendo os acessos dos colaboradores
#com nome de usuario e senha. em seguida peça as informações e valide o login do usuário.



# login ={'kay': '123',
#         'Mika': '321',
#         'Edu': '333',
#          }

# usuario = input('Informe seu USUÁRIO: ')
# senha = input('Digite sua senha: ')

# if usuario in login.keys() and login[usuario] == senha:
#     print('Bem vindo de volta!')
# else:
#     print('usuario e (ou) senha estão incorretos')
 



# print(login['kay'])
# login['kay']= 2023
# print(login['kay'])
# login['ramo'] = 'lala'
# print(login['ramo'])

'''
login ={'KAY': '123',
        'MIKA': '321',
         }

usuario_senha= {}
usuario = input('Informe seu USUÁRIO: ').upper()
senha = input('Digite sua senha: ')
usuario_senha[usuario] = senha

for chave in login.keys():
    if chave == usuario:
        print('usario ok')
        if login[chave] == senha:# usuario_senha[usuario]
            print('Acesso liberado!')
            break
        else:
            print(f'senha incorreta para o usuario {usuario}')
            break
else:
        print(f'o usuário {usuario} não foi encontrado')
'''
#####################################################################################
#QUESTÃO 06
# faça um quiz utilizando um dicionário com as seguintes chaves:
# PERGUNTA, OPÇÕES E RESPOSTA. Faça validação da opção escolhida com a resposta
# e imprima.
######################################################################################

                                            # Matrizes em python

# matriz = [[1,2,3], 
#           [4,5,6],
#           [7,8,9],
# ]

# print(matriz[4][0])
# print(matriz [1][1])

'''
matriz = { 'inicio':[1,2,3], 
          'meio': [4,5,6],
          'fim': [7,8,9],
}

print(matriz['fim'][2])
'''

# print("*"*30)
# print('QUIZ DO AV')
# print("*"*30)

# quiz = {
#         'perguntas': ['quantos orgãos o ser humano tem?',
#                       'quantos ossos o corpo humano tem?',
#                      'quantos musculos o ser humano tem?',
#                 'quantas articulações o ser humano tem?'
#                 ], 

#         'opções': [600, 365, 206, 78,],

#         'respostas': [78, 206, 600, 365]
#     }


    


#     print('resposta incorreta')

quiz = {
     "perguntas": [
       "Qual é a capital do Brasil?",
       "Quem pintou a Mona Lisa?",
       "Qual é o maior planeta do sistema solar?"
     ],
     "opções": [
       ["Rio de Janeiro", "Brasília", "São Paulo"],
       ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh"],
       ["Júpiter", "Terra", "Marte"]
     ],
     "respostas": [1, 0, 0]  
   }
   
pontuacao = 0
for i in range(len(quiz["perguntas"])):
       print("Pergunta:", quiz["perguntas"][i])
       print("Opções:")

       for j in range(len(quiz["opções"][i])):
         print(j, "-", quiz["opções"][i][j])
       resposta = int(input("Digite o número da opção correta: "))

       if resposta == quiz["respostas"][i]:
         pontuacao += 1
         print("Resposta correta!")
       else:
         print("Resposta incorreta!")
print("Pontuação final:", pontuacao, "de", len(quiz["perguntas"]))



