class Pessoa:
    nome = 'Geisa'
    def __str__(self):
        return(f'O nome é {self.nome}')

class Empregado:
    cargo = 'vendedor'
    salario = 3500

class Estudante(Pessoa):
    matricula = 232323
    def __str__(self):
        return(f'O aluno é {self.nome} sua matricula é {self.matricula} e seu curso é de {EstudanteGraduacao.curso}')

class EstudanteGraduacao:
    curso = 'engenharia'

class EstudantePos:
    orientador = 'Sergio'
    nivel = 1

print(f'{Pessoa()}\n{Estudante()}')
# meu_nome.exibir_nome()
# print(f'O nome é: {nome.nome}')