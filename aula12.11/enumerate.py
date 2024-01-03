'''
O método enumerate() é usado em Python para iterar sobre uma 
sequência (como uma lista ou uma string) e retornar um objeto enumerado. 
O objeto enumerado é uma tupla que contém um contador e o valor correspondente da sequência.
O contador começa em 0 por padrão, mas pode ser definido para começar em qualquer número.

Aqui está um exemplo simples de como usar o método enumerate() em Python:

frase = "Olá, mundo!"
for i, letra in enumerate(frase):
    print(i, letra)

saida: 

0 O
1 l
2 á
3 ,
4  
5 m
6 u
7 n
8 d
9 o
10 !

Observe que o método enumerate()
 retorna uma tupla contendo o índice e o valor correspondente da sequência.
   Neste exemplo, a sequência é a string “Olá, mundo!”.

'''

# frase = "Olá, mundo!"
# for i, letra in enumerate(frase):
#     print(i, letra)


def quebraFrase(s):
    
    ultimaLetra= s[-1]
    resto= s[:-1]
    if s=='':
        return

    quebraFrase(resto)

    print(ultimaLetra)

    quebraFrase('cachorro')

quebraFrase('oii')
