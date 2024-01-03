#ESTENDER --> Herança
# Dunder método => __metodo__ (exemplo __init__)
class Estudante:
    nome = 'Paulo'
    matricula = 353637

class EstudanteGraduacao(Estudante):
    curso = 'ADS'
    def __str__(self):
        return(f'Nome: {self.nome}, matricula: {self.matricula} e curso: {self.curso}')
    # curso = 'ADS'
    # def imprimir(self):
    #     print(f'Nome: {self.nome}, matricula: {self.matricula} e curso: {self.curso}')
class EstudantePos(Estudante):
    nivel = 1
    orientador = 'Professor Carlos Alberto'



aluno = EstudanteGraduacao()
print(f'Olá {aluno.nome} seu curso de Graduação é o de {aluno.curso} e sua matricula de acesso é {aluno.matricula}')

print()

print(aluno)# aluno.imprimir()
aluno2 = EstudantePos()
print(f'Olá, {aluno2.nome} seu nivel é {aluno2.nivel} e seu tutor será o {aluno2.orientador}')