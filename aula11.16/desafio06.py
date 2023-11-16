# peça cinco nomes e coloque os nomes em uma lista
# Se o nome iniciar com Consoante avise "Seu nome inicia com Consoante"
# adicone um nome no inicio da lista e imprima a lista

nome1 = input('Digite o nome: ')
nome2 = input('Digite o nome: ')
nome3 = input('Digite o nome: ')
nome4 = input('Digite o nome: ')
nome5 = input('Digite o nome: ')  

# nomes = [nome1, nome2, nome3, nome4, nome5]
# print(nomes)

if (nome1[0]  != "a" and nome1[0] != "e" and nome1[0] != "i" and nome1[0] != "o" and nome1[0] !="u"):
    print("o nome 1 inicia com consoante")
if (nome2[0]  != "a" and nome2[0] != "e" and nome2[0] != "i" and nome2[0] != "o" and nome2[0] !="u"):
    print("o nome 2 inicia com consoante")   
if (nome3[0]  != "a" and nome3[0] != "e" and nome3[0] != "i" and nome3[0] != "o" and nome3[0] !="u"):
    print("o nome 3 inicia com consoante")
if (nome4[0]  != "a" and nome4[0] != "e" and nome4[0] != "i" and nome4[0] != "o" and nome4[0] !="u"):
    print("o nome 4 inicia com consoante")
if (nome5[0]  != "a" and nome5[0] != "e" and nome5[0] != "i" and nome5[0] != "o" and nome5[0] !="u"):
    print("o nome 5 inicia com consoante")

nomes = [nome1, nome2, nome3, nome4, nome5]
nomes.insert(0, "Paulo")
print(nomes)