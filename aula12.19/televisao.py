class Televisao:
    def __init__(self, tamanho):
        self.tamanho = tamanho #inteiro
        self.canal = 0 #inteiro
        self.ligada = False #boleano
        
        #GETs: 
    def get_tamanho(self):
        return self.tamanho
    
    def get_canal(self):
        return self.canal
    
        #SETs:
    
    def set_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho

    def set_canal(self, novo_canal):
        if self.ligada == True and novo_canal >= 0 and novo_canal <= 999:
            self.canal = novo_canal

        #PRÓPRIOS:
    def ligar(self):
        self.ligada = True
        # return self.ligada
        print(f'A TV está ligada!')

    def desligar(self):
        self.ligada = False
        # return self.ligada
        print(f'A tv está desligada')

    def valida_ligada(self):
         if self.ligada == True:
              return 'Ligada'
         else:
              return 'Desligada'
    def __str__(self):
         return f' Sua tv esta {self.valida_ligada()} o canal esta em { self.canal } e o tamanho dela é: {self.tamanho}'

#CHAMADAS DE CRIÇÃO:
tv = Televisao(32)
tv.ligar()
tv.desligar()

tv.ligar()
tv.set_canal(10)
print(tv.get_canal())
print(tv)

