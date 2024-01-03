class CaixaRegistradora:
    def __init__(self, total_da_compra, qttd_recebida):
        self.fundo_caixa = 100.00
        self.total_da_compra = total_da_compra
        self.status = False
        self.qttd_recebida = qttd_recebida


    def get_total_compra(self):
        return self.total_da_compra
    
    def set_total_compra(self, novo_total):
        if self.abrir_caixa == True:
            self.total_da_compra = novo_total
            print(f' voce gastou {self.total_da_compra}')
        else:
            print('caixa fechado')

    def get_qttd_recebida(self):
        return self.qttd_recebida
    
    def set_qttd_recebida(self, novo_qttd_recebida):
        if self.abrir_caixa == True:
            self.total_da_compra = novo_qttd_recebida
            print(f'Voce pagou {self.qttd_recebida}')
        else:
            print('Caixa fechado')

    def abrir_caixa(self):
        self.status = True
        return f'caixa aberto'
        
    def fechar_caixa(self):
        self.status = False
        return f'caixa fechado'

    def caixa(self):
        if self.status == True:
            self.fundo_caixa += self.total_da_compra
            return f'caixa é {self.fundo_caixa}'
        else:   
           return 'Caixa fechado'

    def troco(self):
        if self.status == True:
            return  f'{self.qttd_recebida - self.total_da_compra}'
        else:
            return 'Caixa fechado'
        
    
compra1 = CaixaRegistradora(300, 400)
print(compra1.abrir_caixa())
print(compra1.troco())
print(compra1.caixa())
print()
compra1.set_total_compra(200)
compra1.set_qttd_recebida(400)
print(compra1.troco())
print(compra1.caixa())
print(compra1.fechar_caixa())

    
