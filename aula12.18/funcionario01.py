class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus
    def __str__(self):
        return f'O funcionario {self.nome}, recebe o salario de: {self.salario}, e recebe o bonus de {self.bonus}'
    
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem
    def __str__(self):
        return f'A funcionaria {self.nome}, recebe o salario de: {self.salario} programando em {self.linguagem}'


gerente1 = Gerente("João", 5000, 1000)
desenvolvedor1 = Desenvolvedor("Maria", 3000, "Python")

print(f'{gerente1}\n{desenvolvedor1}')