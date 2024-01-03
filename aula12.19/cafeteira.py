class Cafeteira:
    compartimento_filtro = False
    compartimento_agua = False
    cafe_pronto = False
    ligada = False

    def ligar(self):
        self.ligada = True
        print('Cafeteira esta ligada! ')

    def desligar(self):
        self.ligada = False
        print('Cafeteira desligada!')
    
    def colocar_filtro(self):
        if self.ligada == True:
            if self.compartimento_filtro == False:
                print('Favor colocar água no compartimento')
        else: 
            self.compartimento_filtro = True

    def valida_cafe(self):
        if self.compartimento_filtro == True and self.compartimento_agua == True:
            self.cafe_pronto = True

    def print_cafe(self):
        if self.cafe_pronto == True:
            return 'Cafe pronto'
        else: 
            return 'Aguarde...'
        
    def __str__(self):
        return f'Se café esta {self.print_cafe()},'


