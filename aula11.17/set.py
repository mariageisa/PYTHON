 # SET são conjuntos e esses conjuntos no python são os mensmos conjuntos que aprendemos nas
#escolas caracteristicas: Não teem indice, não garantem ordem de elementos< são interaveis(for, in, not, in),
#sao muitaveis mas so aceitam tipos imutaveis dentro dele, nao podem conter elementos duplicados

#parametro: {}
# metadados: add, update, clear e discard
# criando um set: set('Paulo') ou {1,3,5,7}

#IMUTAVEL

set04 = {1,2,3,4,5}
set05 = {4,5,6,7,8}

set06 = set04 | set05 #união de conjuntos
print(set06)

set06 = set04 & set05 #intersessão de conjuntos
print(set06)

set06 = set04 - set05 #diferença do primeiro p segundo
print(set06)