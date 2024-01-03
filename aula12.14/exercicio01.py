'''
Crie um programa que define a classe 'Carro' com um construtor que reeceba
dois parametros, a cor e a marca do carro.
O programa deve criar duas instancias de classe 'carro', c1 e c2, com 
difeentes valores para os parametros cor e marca.
Em seguida, o programa deve imprimir a cor e a marca de cada um dos carros criados.

'''
class Carro:
    def __init__(self, cor, marca):
        self.cor = cor
        self.marca = marca

c1 = Carro('azul', 'Ford')
print("Carro1: ")
print(f'A cor: {c1.cor}\nMarca {c1.marca}')
print()
c2 = Carro('Vermelho', 'Chevrolet')
print('Carro 2: ')
print(f'Cor: {c2.cor}\nMarca {c2.marca}')