''' count -> a função dele é contar quantas vezes um determinado
caractere aparece em uma string!

upper e a lower - dois metodos que deixam toda a string em maiuscula ou minuscula

EXPRESSÕES REGULARES -> ORIENTAÇÃO A OBJETO!

find -> busca por uma expresão dentro da frase

replace -> é utilizado para realizar alterações dentro das strings

capitalize ->deixa a primeira letra das palavras maiiusculas

split-> procura so o que é caractere, transforma sua string em uma lista

'''
frase = "a banana é amarela e o abacate é verde".lower()
letra = "e"

email = 'paulojunior@gmail.com'
print(f'A letra "{letra}" aparece { frase.count(letra)} vezes na frase "{ frase }".')
achei = (frase.find('ana'))

if achei >= 0:
    print(f' A expressão foi encontrada no indice {achei}')
else:
    print(f'A expressão NÃO  foi encontrada na frase')

# saida = input('Digite s para sair; ').upper()
# if saida == 'S':
#     print(saida)

nova_frase = frase.replace('banana', 'maracujá')
nova_frase2 = frase.replace('abacate', 'manga')
nova_frase2 = frase.replace(' ', '')
print(frase)
print(nova_frase)
print(nova_frase2)
print(email.replace(' ', ''))
print(frase.capitalize())
print(frase.split())