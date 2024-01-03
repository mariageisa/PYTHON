# def extrair_vogais(texto):
#     vogais = texto[::2]  # Utilizando fatiamento para extrair as vogais
#     return vogais

# frase = input("Digite uma frase: ")
# resultado = extrair_vogais(frase)
# print(resultado)


''' a função `extrair_vogais` recebe uma string como entrada e utiliza o fatiamento (`[::2]`) 
para extrair apenas as vogais presentes na string. O resultado é retornado pela função e impresso na tela.'''

def extrair_vogais(texto):
    consoantes = ''
    for letra in texto:
        if letra.lower() not in 'aeiou':
            consoantes += letra
    return consoantes

frase = input("Digite uma frase: ")
resultado = extrair_vogais(frase)
print(resultado)