from interface import Icampeao

class personagem:   #classe contexto

    def __init__(self,campeao ):
        self.campeao = campeao

    def tipo_habilidade(self):
        self.campeao.habilidade()

    def nivel_habilidade(self):
        self.campeao.nivel_de_luta()

    def tipo_combate(self):
        self.campeao.estilo_de_combate()


