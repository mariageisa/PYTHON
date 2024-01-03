'''
isdecimal()
isnumeric()
# numero = input('Digite um numero: ')
# if numero.isdigit() == True:
#     print('Ok é um numero')
'''
class Pet: 
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.fome = 0
        self.comida = 100
        self.sede = 0
        self.agua = None


#OS GETS:
    def get_nome(self):
        return self.nome
    
    def get_peso(self):
        return self.peso 
   
    def get_fome(self):
        return self.fome
    
    def get_sede(self):
        return self.sede
    
#OS SETS:
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_peso(self, novo_peso):
        self.peso = novo_peso

    def set_fome(self, nova_fome):
        self.fome += nova_fome
        
        while self.fome >=99:
            diferenca = self.fome - 99
            print(f'Voce deve alimentar pelo menos {diferenca} de comida ao {self.nome}')
            print(f'Alimente o {self.nome}')
            nova_comida = int(input('Quanto de comida vc quer dar para o seu pet? '))
            self.comida -= nova_comida
            self.fome -= nova_comida

    def set_sede(self, nova_sede):
        self.nome = nova_sede

    def imprimir(self):
        print(f'Olá, me chamo {self.nome}')
        print(f'estou pesando {self.peso}')
        print(f'minha fome está em {self.fome}')
        print(f'Minha sede esta em {self.sede}')

caozinho = Pet('Atlas', 17)

# caozinho.imprimir()
caozinho.set_fome(20)
caozinho.imprimir()
caozinho.set_fome(30)
caozinho.imprimir()
caozinho.set_fome(70)
caozinho.imprimir()
caozinho.set_fome(10)
caozinho.imprimir()

