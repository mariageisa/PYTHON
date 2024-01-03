'''
DICIONÁRIO ---> em uma lista de dicionario voce terá várias informações! ( SÃO UMA EVOLUÇÃO DOS conjuntos n tem indices SETS)
DICIONÁRIOS SÃO MUTÁVEIS E CONTER VALORES DE DIFERENTES TIPOS!
/CHAVE --> VALOR
d = {user: "marcelo" , "password": 2343}

Dicionarios n são ordenados assim como os conjuntos (sets)

ALGUNS METODOS:
has_key('eggs'), clear(), del d[key], keys(), values(), items(), get(), update()

copy() fazer copias de dicionarios! lembre-se que dicionario é mutável!!!

item do dicionario = chave e valor!

sorted - ordena na forma crescente 
sorted(d, key = d.get, reverse=True) - ordem decrescente

'''

#possuem CHAVE(KEYS) e VALOR(VALUES)
# Parametro: {} ou dict()

#Dicionário é uma coleção que é ordenada** e mutável. Sem membros duplicados.
pessoa = { 'nome': 'Paulo',
          'sobrenome': 'Junior1',
          'nome 2': 'Rodrigo',
          'sobrenome': 'Junior',
          'sobrenome': 'Junior4' }

# LEN retornará o tamanho do dicionario
print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())

k = pessoa.keys()
v = pessoa.values()


for chave in  k:
    print(chave)
    print("*"*20)

for chave in v:
    print(chave)

for chave, valor in pessoa.items():
    print(chave, valor)

i = pessoa.items()
print("*"*20)


# imprimir o valor pela chave
print(pessoa['sobrenome'])
print(pessoa['nome'])

print("*"*30)

d1 = {'valor1': 100,
      'valor2': 200,
      'valor3': 300,}

# apenas um apontamento para o dicionário
d2 = d1.copy()
#com COPY terá vvalor proprio

print(d1)

d2['valor2'] = 'Geisa'

print(d1)
print(d2)

print(d2.get('valor2'))


#NÃO PRECISA DE POP POIS HÁ O DEL!
d3 = d1.pop('valor3')

print(d1)


# NÃO CONSEGUIMOS ATUALIZAR O DICIONARIO COM OUTROS TIPOS DE DADOS

outro_nome = {'valor5': 5,
              'valor6': 6, }
# lista = [1, 2, 3]
d1.update(outro_nome)
print(d1)

print(d1.has_key('valor5'))