# Crie uma abstração para uma super classe funcionário com duas sub Classes.Imprima todos os dados.

class Funcionario:
    def __init__ (self, nome, horario, funcao):
         self.nome = nome
         self.horario = horario
         self.funcao = funcao


class Piloto(Funcionario):
     salario = '45.000'
     def __str__(self):
          return f'O funcionario {self.nome} chegou as: {self.horario}, sua função na cia áerea é de {self.funcao} seu salário é de {self.salario}'
     
class Aeromoca(Funcionario):
     salario = '23.00'
     def __str__(self):
          return f'A funcionária {self.nome} chegou as: {self.horario}, sua funcão na cia aérea é de {self.funcao} seu salário é de {self.salario}'
  
     
fucionario = Piloto('JUNGKOOK', '8:00', 'piloto')
fucionaria = Aeromoca('Je', '7:00', 'aeromoça')

print(f'{fucionario}\n {fucionaria}')
          