class Automovel:
    def __init__(self, placa, cor):
        self.__placa = placa
        self._cor = cor

    def get_placa(self):
        return self.__placa 
    
    def get_cor(self):
        return self._cor
    
    def set_cor(self, nova_cor):
        self._cor = nova_cor

    def dirigir(self, velocidade):
        print(f'estou dirigindo a {velocidade} km/h')

#INSTANCIAS
carro = Automovel('THC-212', 'vermelho')
moto = Automovel('DSF-889', 'preto')
caminhao = Automovel('QAQ- 384', 'Amarelo')

#CHAMADAS GET:
print(f' A cor do carro é {carro.get_cor()} e a placa é {carro.get_placa()}')
print(f' A cor da moto é {moto.get_cor()} e a placaa é {moto.get_placa()}')
print(f' A cor do caminhão é {caminhao.get_cor()} e a placa é {caminhao.get_placa()}')
print()

#CHAMADAS SET:
carro.set_cor('BRANCO')
moto.set_cor('ROSA')
caminhao.set_cor('AZUL')

#NOVAS CHAMADAS GET É:
print(f' A cor do carro é {carro.get_cor()} e a placa é {carro.get_placa()}')
print(f' A cor da moto é {moto.get_cor()} e a placaa é {moto.get_placa()}')
print(f' A cor do caminhão é {caminhao.get_cor()} e a placa é {caminhao.get_placa()}')

print()
carro._cor('LOLOLOO')
print(f' A cor do carro é {carro.get_cor()} e a placa é {carro.get_placa()}')

#TODA VIDA Q USAR O PROPETY ELE DEVE SER PRIVADO