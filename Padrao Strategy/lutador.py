from interface import Icampeao

class lutador(Icampeao):

    def __init__(self,nivel):
        self.nivel = nivel

    def habilidade(self):
        print("usa armas corpo a corpo")

    def nivel_de_luta(self):
        print(f"nivel de luta {self.nivel}")

    def estilo_de_combate(self):
        print("ataca de curta distancia")
