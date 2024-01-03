''' Escreva um código que, recebe três palavras e uma frase, crie uma função que verifique se as
 palavras aparecem COMPLETAS na frase e indique qual intervalo de índices ele foi encontrada. Você deve 
 utilizar uma lista para realizar a atividade.

Obs.: você deve validar se a palavra tem três ou mais letras
Obs.: você deve validar se a frase tem pelo menos 20 palavras'''

# função que verifica se as palavras aparecem COMPLETAS na frase:
def verificar_palavras():
    #Usando o splite tornei a variavel em lista e posso trabalhar com seus indices
    palavra = input('Digite três palavras separadas por espaço: ').upper().split()
    #encontro o comprimento da palavra usando o len e o indice
    #onde se encontra a palavra e comparo se seu tamanho é menor que 3
    if (len(palavra[0])) < 3 or (len(palavra[1])) <3 or (len(palavra[2]) <3):
        print("As palavras devem ter pelo menos três letras.")
        palavra = input('Digite três palavras separadas por espaço: ').split()

    frase = input('Digite uma frase: ').upper()
    #usand o split para desmenbrar a string e usando len para saber seu comprimento é maior que 25
    if len(frase.split()) < 3:
        print("A frase deve ter pelo menos 20 palavras.")
        return
    #uma nova variavel que recebera a frase como lista
    palavras = frase.split()

    # Percorre a lista de palavras e verifica se cada palavra fornecida aparece completa na frase
    for i in range(len(palavras)):
        if palavras[i] == palavra[0]:
            print(f"A palavra '{palavra[0]}' foi encontrada no intervalo de índices [{i}, {i + len(palavra)}].")
        if palavras[i] == palavra[1]:
            print(f"A palavra '{palavra[1]}' foi encontrada no intervalo de índices [{i}, {i + len(palavra)}].")
        if palavras[i] == palavra[2]:
            print(f"A palavra '{palavra[2]}' foi encontrada no intervalo de índices [{i}, {i + len(palavra)}].")

verificar_palavras()