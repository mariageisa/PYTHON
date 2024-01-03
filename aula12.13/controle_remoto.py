class ControleRemoto:

    def __init__(self, cor, marca, qnt_pilhas):
        self.botao = None #ainda n foi pressionado
        self.cor= cor
        self.marca = marca
        self.qnt_pilhas = qnt_pilhas
        self.painel = False #pq esta desligado
        self.temperatura = 0

        #METODOS:
    def ligar(self):
        self.painel = True

    def desligar(self):
        self.painel = False

    def set_temperatura(self, nova_temperatura): #set p mudar a trmperatura
        if self.painel == False:
            print('temperatura nao pode ser alterada. Ar desligado.')
        else:
            self.temperatura = nova_temperatura

    def get_tempertura(self):
        return self.temperatura

    def pressionar_botao(self, tipo_de_botao):
        self.botao = tipo_de_botao
        if self.botao == 'Ligar' and self.temperatura == 0:
            print('Ar está ligado')
            self.ligar()
        elif self.botao == 'Desligar':
            print('Ar esta desligado')
        self.set_temperatura(0)
        self.desligar()
        
controle = ControleRemoto('branco', 'elgin', '2') 
controle.pressionar_botao('Ligar')
controle.set_temperatura(20)


