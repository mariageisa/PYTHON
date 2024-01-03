class FoneDeOuvido:

    def get_volume(self):
        print(F'entrei no get')
        return self.__volume
    
    def set_volume(self, novo_volume):
        print(F'entrei no set com o volume de {novo_volume}')
        self.__volume = novo_volume
    #atributo:
    volume = property(get_volume, set_volume)
    
fone = FoneDeOuvido()

fone.set_volume(100) #SET

fone.get_volume()#GET

fone.volume = 200 #SET