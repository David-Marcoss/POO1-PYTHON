
class televisao:
    def __init__(self,total_canais=10,max_volume=10):
        self.total_canais = total_canais
        self.max_volume =  max_volume

class controleremoto:
    def __init__(self,canal_atual=1,volume_atual=0):
        self.canal_atual = canal_atual
        self.volume_atual = volume_atual
        self.televisao = televisao()

    def aumentar(self):
        if( self.volume_atual < self.televisao.max_volume):
            self.volume_atual+=1
            return True
        else:
            return False

    def diminuir(self):
        if( self.volume_atual > 0):
            self.volume_atual-=1
            return True
        else:
            return False
    def passarcanal(self):
        if( self.canal_atual < self.televisao.total_canais):
            self.canal_atual+=1
            return True
        else:
            return False

    def voltarcanal(self):
        if( self.canal_atual > 1):
            self.canal_atual-=1
            return True
        else:
            return False
    def trocarcanal(self,canal):
        if(canal > 0 and canal <= self.televisao.total_canais):
            self.canal_atual = canal
            return True
        else:
            return False

    def vervolume(self):
        return self.volume_atual

    def vercanal(self):
        return self.canal_atual
