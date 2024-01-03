# nome = 'Paulo'
# texto = iter(nome)
# print(next(texto))
# print(texto)
# for letra in nome:
#     print(letra)

lista_nomes = ['Joao', 'Pedro', 'Mateus', 'Judas', 'Tiago']
lista_enumerada = enumerate(lista_nomes)
print(lista_nomes)
print(list(lista_enumerada))#transformar o iteravel em uma lista de (tuplas)

for item in lista_enumerada:
    print(item)

# for item_lista in lista_nomes:#Retorna nomes e n é interessante trabalhar com isso
#     print(item_lista)

for indice_lista, item_lista in enumerate(lista_nomes):
    print(f'{item_lista} é o {indice_lista} da lista')