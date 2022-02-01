from interface import Icampeao

class atirador(Icampeao):

    def __init__(self,nivel):
        self.nivel = nivel

    def habilidade(self):
        print("usa armas de fogo")

    def nivel_de_luta(self):
        print(f"nivel de luta {self.nivel}")

    def estilo_de_combate(self):
        print("ataca de media ou longa distancia")
