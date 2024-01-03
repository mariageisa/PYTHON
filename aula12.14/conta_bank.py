#Projeto de conta Bancaria
#Atributos: nome, saldo
#Metodos: Mostrar saldo, sacar, depositar

#Adicione novas funcoes:
#1. histórico de depósito de saque
#2. taxas para saque
#3. Limite o saque após sacar o valor x
#4. Transferencia entre contas!!!

class ContaBancaria:
    def __init__(self, nome_titular, saldo_inicial):
        self.nome_titular = nome_titular
        self.saldo = saldo_inicial
        self.extrato = []

    def exibir_saldo(self,):
        print(f'Saldo atual: R$ {self.saldo}')

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
        self.extrato.append("+ R$ " + str(valor_deposito))
        print(f'O valor r$ {valor_deposito} foi depositado')
        self.exibir_saldo() 

    def sacar(self, valor_saque):
        if valor_saque > self.saldo:
            print('Saldo insuficiente!')
        else:
            self.extrato.append("- R$ " + str(valor_saque))
            self.saldo -= valor_saque
            print(f'Valor R$ {valor_saque} foi sacado!')

    def exibir_extrato(self):
        print("\nEXTRATO:")
        for item in self.extrato:
            print(item)

print('conta 1 : ')
conta1 =ContaBancaria("Roberto", 60)
conta1.depositar(20)
conta1.sacar(30)
conta1.exibir_extrato()


