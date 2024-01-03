''' 
Crie um programaa que deefine a classe "aluno" com um cosntrutor
que recebe três parametros, o nome, a idade e a nota do aluno.
O programa deve criar duas instancias da classe "aluno", "a1" e "a2"
com diferentes valores para cada parâmetro nome, idade e nota.

Em seguida, o programa deve imprimir o nome, a idadde e a nota de ccada aluno
criado. e por ultimo , calcular e imprimir a media das notas dos dois 
alunos criados.
'''

class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

print('Aluno 01: ')
a1 = Aluno("Barbie", '30', 10)
print(f'o aluno(a) {a1.nome}\nidade: {a1.idade}\nNota: {a1.nota} ')
print('-'*25)
print('Aluno 02: ')
a2 = Aluno("Ken", '28', 7)
print(f'o aluno(a) {a2.nome}\nidade: {a1.idade}\nNota: {a1.nota} ')
print('-'*25)
print('Media: ')
media = (a1.nota + a2.nota) /2
print(f'A media de notas foi {media}')