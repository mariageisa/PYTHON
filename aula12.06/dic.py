'''CRUD --> Criar, Ler, Atualizar, Deletar'''

dic = { 'nome': 'paulo'}# created
dic2 = dict(idade=23)# createt
dic['nome']#READED
reading = dic2.get('idade')#READED
dic.update(sobrenome ='junior')# UPDATE ou inserindo novos itens de forma direta
dic.update({'idade': 23})#UPDATE

'''QUANDO vai adicionar apenas uma tupla deverá usar uma , UM INTERÁVEL'''
tupla = ('peso', 72.12), #UPDATE
dic.update(tupla)
lista = ['data ', '13/04/1996'],['numeros',[1,2,3,4,5,6,7,8,9] ]#UPDATE
dic.update(lista)
print(dic)
print(dic2)

dic.clear() #deleted

print(f'Dados do dicionário: {dic}')