#Faça um código que leia um nome de um usuário e a sua senha e não aceite
#a senha igual ao nome do usuário, mostrando uma mensagem de erro e pedindo as informações
#novamente


while True:
    nome = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')
    if nome == senha:
        print('ERROR:USUARIO E SENHA NÃO PODEM SER IGUAIS! ')
    elif nome != senha:
        print('Voce entrou')
        break


# FERRARI DO PROFESSOR:
# tentativas = 1
# while tentativas <= 3:
#     usuario = input('Informe seu usuario: ')
#     senha = input('Informe sua senha: ')
#     if senha == usuario:
#         print(F'ERROR: essa tentativa foi a numero {tentativas} ')
#         if tentativas == 3:
#             print(f'Suas tentativas acabaram. Tente amanhã')
#             break
#     else:
#         print(f'Acesso liberado')
#         break
#     tentativas = tentativas + 1


