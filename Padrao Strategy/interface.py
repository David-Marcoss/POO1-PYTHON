import abc


class Icampeao(abc.ABC):  #classe estrategia

    @abc.abstractmethod
    def habilidade(self):
        pass

    @abc.abstractmethod
    def nivel_de_luta(self):
        pass

    @abc.abstractmethod
    def estilo_de_combate(self):
        pass
