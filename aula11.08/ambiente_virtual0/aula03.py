#OPERADORES IN E NOT IN 
nome = "Paulo"
print('' in nome)

print('='*20)

seu_nome = input('informe seu nome: ')
buscar = input('Informe o valor a ser encontrado: ')

if ( buscar in seu_nome ):
    print(f'{buscar} está contido em {seu_nome}')
else:
    print(f'{buscar} nao está contido em {seu_nome}')


