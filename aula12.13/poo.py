#     #usar __init__ construtor(atributos)
# class Automovel:
    # #ATRIBUTOS:
    # def __init__ (self, placa = 'XYZ-4925'):
#         self.placa = placa
#     #METODOS:
#     def get_placa(self):
#         return self.placa
    # def dirigir(self, velocidade):
    #     print(f'Estou dirigindo a {velocidade} km/h')

# '''ESTANCIA:(OBJETO DA CLASSE ACIMA)'''
# carro = Automovel()#parenteses pq é uma classe sem eles eles vai pensar q é algum valor
# print(carro.get_placa())
# carro.dirigir(220)

'''
class Automovel:
    #ATRIBUTOS:
    def __init__ (self, placa):
        self.placa = placa
    def get_placa(self):
        return self.placa
    def dirigir(self, velocidade):
        print(f'Estou dirigindo a {velocidade} km/h')

carro = Automovel('DHC- 123')
print(carro.get_placa())
carro.dirigir(223)

moto = Automovel('HCG- 343')
print(moto.get_placa())

'''

class Automovel:
    #ATRIBUTOS:
    def __init__ (self, placa, cor):
        self.placa = placa
        self.cor = cor
    #METODOS:
    def get_placa(self):
        return self.placa
    def dirigir(self, velocidade):
        print(f'Estou dirigindo a {velocidade} km/h')
    def get_cor(self):
        return self.cor
    def set_cor(self, nova_cor): #Set eu altero!
        self.cor = nova_cor

carro = Automovel('SHW- 232', 'preto')
print(carro.get_cor())

# carro.set_cor('vermelho')
# print(carro.get_cor())