class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #GETS
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    #SETS:
    def imprimir(self):
        print(f'Olá, me chamo {self.nome}')
        print(f'nasci em ')

p1 = Pessoa('lana', 34)
p1.imprimir()
p1.get_ano_nascimento()