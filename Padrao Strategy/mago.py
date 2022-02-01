from interface import Icampeao

class mago(Icampeao): # classes concretas que impelmentao a solução

    def __init__(self,nivel):
        self.nivel = nivel

    def habilidade(self):
        print("usa magias")

    def nivel_de_luta(self):
        print(f"nivel de luta {self.nivel}")

    def estilo_de_combate(self):
        print("ataca de curta ou media distancia")
