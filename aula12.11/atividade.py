''' Escreva um código que, recebe três palavras e uma frase, crie uma função que verifique se as
 palavras aparecem COMPLETAS na frase e indique qual intervalo de índices ele foi encontrada. Você deve 
 utilizar uma lista para realizar a atividade.

Obs.: você deve validar se a palavra tem três ou mais letras
Obs.: você deve validar se a frase tem pelo menos 20 palavras'''


# def verificar_palavras(palavra1, palavra2, palavra3, frase):

#     # Verifica se as palavras têm pelo menos três letras
#     if len(palavra1) < 3 or len(palavra2) < 3 or len(palavra3) < 3:
#         print("As palavras devem ter pelo menos três letras.")
#         return
    
#     # Verifica se a frase tem pelo menos 20 palavras
#     if len(frase.split()) < 5:
#         print("A frase deve ter pelo menos 20 palavras.")
#         return
    
#     # Divide a frase em uma lista de palavras
#     palavras = frase.split()
    
#     # Percorre a lista de palavras e verifica se cada palavra fornecida aparece completa na frase
#     for i in range(len(palavras)):
#         if palavras[i] == palavra1:
#             print(f"A palavra '{palavra1}' foi encontrada no intervalo de índices [{i}, {i + len(palavra1)}].")
#         elif palavras[i] == palavra2:
#             print(f"A palavra '{palavra2}' foi encontrada no intervalo de índices [{i}, {i + len(palavra2)}].")
#         elif palavras[i] == palavra3:
#             print(f"A palavra '{palavra3}' foi encontrada no intervalo de índices [{i}, {i + len(palavra3)}].")

# palavra1 = input('Digite uma palavra: ')
# palavra2 = input('Digite uma palavra: ')
# palavra3 = input('Digite uma palavra: ')
# frase = input('Digigte uma  frase')
# verificar_palavras(palavra1, palavra2, palavra3, frase)






# def verificar_palavras(palavras, frase):
    
#     indices_encontrados = [i for i, palavra in enumerate(frase.split()) if len(palavra) >= 3 and palavra in palavras]
    
#     if len(indices_encontrados) == 3:
#         return f"As palavras foram encontradas nos índices: {indices_encontrados}."
#     else:
#         return "Algumas palavras não foram encontradas na frase."

# palavras = input("Digite as três palavras separadas por espaço: ").split()
# frase = input("Digite a frase: ")

# resultado = verificar_palavras(palavras, frase)
# print(resultado)
#########################################
# lista=['Curso','Python','Progressivo']

# #Unindo as palavras com vírgula
# print( ','.join(lista) )

# #Unindo as palavras com espaço
# print( ' '.join(lista) )

##################################################################################################################
'''
como usar o join em uma lista que recebeu dados de dois inputs?



você pode transformar essas entradas em elementos de uma lista e passa-la como parâmetros da função join(), assim:
nome = 'joao'
sobrenome = 'sila'
completo = ' '.join([nome, sobrenome])
print(completo)
'''
###################################################################################################################

# def verificar_palavras(palavra1, palavra2, palavra3):
#     palavra1 = input('Digite uma palavra: ')
#     palavra2 = input('Digite uma palavra: ')
#     palavra3 = input('Digite uma palavra: ')
#     frase = input('Digite uma frase: ')

#     if palavra1 <3 or palavra2 <3 or palavra3 <3:
#         print('A palavra deve ccontermais de 3 letras!')
#         return
#     if len(frase.split()) < 5:
#         print('Frase deve conter mais de 5 palavras! ')
#         return
#     palavras = frase.split()

#     for i in range(len(palavras)):

    
# verificar_palavras()

# def verificar_palavras():

#     # Verifica se as palavras têm pelo menos três letras
#     palavra1 = input('Digite uma palavra: ')
#     palavra2 = input('Digite uma palavra: ')
#     palavra3 = input('Digite uma palavra: ')

#     frase = input('Digite uma frase: ')
#     if len(palavra1) < 3 or len(palavra2) < 3 or len(palavra3) < 3:
#         print("As palavras devem ter pelo menos três letras.")
#         return input('digite uma palavra novamente: ')

#     if len(frase.split()) < 3:
#         print("A frase deve ter pelo menos 20 palavras.")
#         return
    
#     palavras = frase.split()
    
#     # Percorre a lista de palavras e verifica se cada palavra fornecida aparece completa na frase
#     for i in range(len(palavras)):
#         if palavras[i] == palavra1:
#             print(f"A palavra '{palavra1}' foi encontrada no intervalo de índices [{i}, {i + len(palavra1)}].")
#         elif palavras[i] == palavra2:
#             print(f"A palavra '{palavra2}' foi encontrada no intervalo de índices [{i}, {i + len(palavra2)}].")
#         elif palavras[i] == palavra3:
#             print(f"A palavra '{palavra3}' foi encontrada no intervalo de índices [{i}, {i + len(palavra3)}].")


# verificar_palavras()

'''
Para verificar se uma lista de palavras está em uma string em Python sem usar expressão regular,
você pode usar um loop for. Aqui está um exemplo de como você pode fazer isso:

def lista_de_palavras_na_string(lista, string):
    for palavra in lista:
        if palavra in string:
            i = string.index(palavra)
            print(f"A palavra '{palavra}' aparece completa na frase no intervalo [{i}, { i +len(palavra)}]")
    return
Nesse exemplo, a função lista_de_palavras_na_string recebe uma lista de palavras e uma string como entrada. 
Ele usa um loop for para iterar sobre cada palavra na lista e verifica se a palavra está na string. 
Se a palavra estiver na string, a função usa o método index() 
da string para encontrar a posição inicial da palavra na string e imprime o intervalo em que a palavra aparece na string.

Espero que isso ajude! Se você tiver mais alguma dúvida, por favor, não hesite em perguntar.
'''

'''Para verificar se uma lista de palavras está em uma string em Python sem usar expressão regular,
 você pode usar um loop for. Aqui está um exemplo de como você pode fazer isso:'''