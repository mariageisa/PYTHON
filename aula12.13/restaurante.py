class Restaurante:

    def __init__(self, clientes, funcionarios):
        self.clientes = clientes
        self.funcionarios = funcionarios

    def reserva_cliente(self, mesa):
        self.clientes=input('Deseja fazer uma reserva? \nDigite seu nome: ')
        dic_reserva=[]
        hora_disponivel = ['19:00', '19:30', '20:00', '20:30', '21:00']
        # mesa_disponivel = [1,2,3,4,5]
        while True:
                marcar= int(input("1. Exibir horários disponíveis\n"
                  "2. reservar horario\n"))
                if(marcar==1):
                    print(hora_disponivel)   
                     
                if(marcar==2):
                 hora= input('Digite horário desejado: ')
                 dic_reserva.append(hora)

                if dic_reserva in hora_disponivel:
                    print(f'O horário{dic_reserva} está reservado para {self.clientes}')
               
        # dic_indisponivel={'20:00': 'indisponivel',
        #                   '23:00': 'indisponivel'}
        
        # horario_reserva = input('Digite o horario que deseja reservar: ')

        # if horario_reserva in dic_reserva:
        #     print(f'O cliente {self.clientes} reservou o horário: {horario_reserva} na mesa: {mesa}')
        # if horario_reserva in dic_indisponivel:
        #     print(f'o horario já está ocupado!')  
  
restaurante = Restaurante(1, 10)
restaurante.reserva_cliente(2)