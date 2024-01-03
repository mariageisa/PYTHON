'''
Crie um programa que defina a classe 'Circulo' 
com um cosntrutor que receba um parametros, o raio do circulo.
o programa deve criar duas instancias daa classe "circulo", c1 e c2, com diferentes
valores paraa o parametro raio. Em seguida , o programa deve imprimir o raio e 
a área de cada um dos circulos criados.'''

class Circulo:
    def __init__(self, raio):
        self.raio = raio 
        self.area = raio*raio*3.14

print('Circulo 1: ')
c1 = Circulo(3)
print(f'Raio: {c1.raio}\nÁrea: {c1.area}')

print('Circulo 2: ')
c1 = Circulo(2.50)
print(f'Raio: {c1.raio}\nÁrea: {c1.area}')