# # -*- coding: utf-8 -*-

# # Crie uma classe Carro
# # ela deve ter os atributos:
# #   * 4 rodas
# #   * portas
# #   * motor
# #   * vidros
# # e os seguint métodos:
# #   * ligar
# #   * acelerar
# #   * frear
# #   * desligar



# class car():
#     def __init__(self):
#         self.rodas = 4
#         self.portas = 4
#         self.vidros = True
#         self.motor = True
#         self.ligado = False

#     def ligar(self):
#        if self.ligado = True:
#         print('ligando...')
#         print('ligado!')

#     def acelerar(self):
#         if self.ligado ==True:
#         print('acelerando...')
#         self.parado = False
#         else:
#             self.parado = True

#     def frear(self):
#         if self.parado == False:




# fiat = carro()
# fiat.ligar
# fiat.acelerar

class Passaro():
    def __init__(self):
        self.penas = True
        self.asas = 2
        self.bico = True
        self.patas = 2
        self.rabo = True
        self.olhos = 2

    def voar(self):
        print('Passaro voando')
    
    def pousar(self):
        print('Pousando')

    def dormir(self):
        print('Dormindo')

    def comer(self):
        print('comendo')

# Faça uma classe sabia que herde caracteristicas do Passaro
# e as use
# Faça uma galinha que herde caracteristicas de Passo
# e mantenha as suas

class Sabia(Passaro):
    
    def cantar(self):
        print('cantando')
    
class galinha(Passaro):

    def voar(self):
        raise ValueError('Erro: Galinha não voa')
    def pousar(self):
        raise ValueError('Erro: Galinha não voa')
    

p1 = Sabia()
p2 = galinha()

p2.voar()