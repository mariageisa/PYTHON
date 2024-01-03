class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.__cpf = None

    def __str__(self):
        return(f'Nome: {self.nome}, idade:; {self.idade} e cpf: {self.__cpf}')
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, meu_cpf):
        self.__cpf = meu_cpf

# class Professor(Pessoa):
#     def __init__(self, nome, idade, salario, disciplina,cpf ):
#         super().__init__(nome,idade)
#         self.salario = salario
#         self.disciplina = disciplina
#         self.cpf = super().get_cpf(cpf)

#     def __str__(self):
#         return f'Nome: {self.nome}'

# paulo = Professor('Paulo junior', 29, 544443, 'Backend', 979868584)

# print(paulo)
# class Aluno(Pessoa):



# class Homem(Pessoa):
#     pass
# class Mulher(Pessoa):
#     pass

# elvis = Homem('Elvis', '28')
# paula = Mulher('Paula', '19')
    
# elvis.set_cpf(233112345)
# paula.set_cpf(908812345)

# print(elvis)
# print(paula)