class Pikachu:
    tipo = 'Eletrico'

    def __init__(self, nome, hp, amp_max):
        self.nome = nome
        self.hp = hp
        self.amp_max = amp_max

    def atacar(self):
        print(f'O Pikachu {self.nome} ataca com amperaje elétrica de {self.amp_max}')

pikachu1 = Pikachu('Merlin', 2550, 200)
pikachu2 = Pikachu('Akashi', 1000, 1000)

pikachu1.atacar()
pikachu2.atacar()