from random import randint

class Personagem():
    """classe que representa um personagem de um jogo de RPG"""
    def __init__(self, nome, xp=0, nivel=1):
        """Inicializando as propriedades de um personagem"""
        self.nome = nome
        self.hp = 100
        self.mp = 100
        self.xp = xp
        self.nivel = nivel
    
    def subirNivel(self):
        if self.xp > 99:
            self.nivel += 1
            self.xp = 0
            self.hp = 100
            self.hp = (self.hp * (0.10 * self.nivel))
            print('Você subiu de nível!')

    def mataMostro(self, hp_monstro=100):
        self.poderMonstro = randint(1,100)
        if self.poderMonstro > 50:
            self.hp -= 20
            print(f'Você tomou dano! \n{self.hp}')
        else:
            self.hp_monstro = hp_monstro - 40
            print(f'Monstro tomou dano! \n{self.hp_monstro}')
            if self.hp_monstro <= 0:
                self.xp += 10
                self.hp_monstro = 100
                subirNivel()

class Mostro():
    def __init__(self):
        self.nome = 'Monstro_n1'

    def informacao(self):
        print(f'Nome do Monstro: {self.nome}')

class Minotauro(Mostro):
    def __init__(self):
        self.nome = 'Minotauro_n1'

    def informacao(self):
        print(f'Nome do Minotauro: {self.nome}')




m1 = Mostro()
m2 = Minotauro()

m1.informacao()
m2.informacao()



class Mago(Personagem):
    def ataque(self):
        print('Magia das trevas')



class Caveleiro(Personagem):

    def ataque(self):
        print('Colera do dragão')





