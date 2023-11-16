# imprima na tela os pares dentro de uma lista chamada pares_ok
# remova da lista os multiplos de 4

meus_numeros = [0, 1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

meus_numeros.remove(0)
pares_ok =  meus_numeros[1::2]

print(pares_ok)

meus_numeros.remove(4)
meus_numeros.remove(8)
meus_numeros.remove(12)
meus_numeros.remove(16)
meus_numeros.remove(20)

print(meus_numeros)
