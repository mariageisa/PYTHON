# uma lista é representada pelos[colchetes]
# Len - metodo que retorna a quantidade de itens de uma lista OBS: todo metododo por obrigação ele retorna um valor
# append - metododo que insere itens no final da lista
# del - remove item pelo indice especifico da lista 
# remove - remove um objeto especificado da lista
#pop - remove o ultimo objeto da lista (variavel.pop()) ALEM DA LISTA ATUALIZADA DO ULTIMO INDICE, ele retorna o valor do pop
#insert - ele adiciona um objeto no inicio da lista
'''

lista = []

print(lista, type(lista))
print(len(lista))

lista = ['front']
print(lista, type(lista))
print(len(lista))

lista = ['back']
print(lista, type(lista))
print(len(lista))

lista.append('oi')
print(lista, type(lista))
print(len(lista)) '''


# 0    1   2    3    4  
#-5   -4  -3   -2   -1

lista = ['back', 'tarde', 21, True, 8.8 ]

print(f'a quantidade de alunos na turma é: {lista[2]}')

lista[2] = 22
print(lista)

#LISTA DENTRO DE LISTA = MATRIZ
lista[1] = ['Neyva', 'Alice', 'Lara', 'Paula', 'Geisa']
print(lista [1] [2])

print(lista[-2])
del lista[-2]
print(lista)
del lista[-2]
print(lista)
lista.remove('back')
lista.append(26)
lista.append(27)
lista.append(900)
print(lista)
#lista.pop ()
valor_do_pop = lista.pop()
print(valor_do_pop)
lista.insert(0, 'Amontada valley')
print(lista)
lista.insert(2, 'professor')
print(lista)
