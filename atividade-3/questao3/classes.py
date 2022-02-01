class elevador:
    def __init__(self,capacidade,total_andares,andar_atual=0,quant_pessoas=0):
        self._andar_atual = andar_atual
        self._total_andares = total_andares
        self._capacidade = capacidade
        self._quant_pessoas = quant_pessoas

    def entra(self):
        if(self._quant_pessoas<self._capacidade):
            self._quant_pessoas+=1
            return True
        else:
            return False

    def sai(self):
        if (self._quant_pessoas > 0):
            self._quant_pessoas -= 1
            return True
        else:
            return False

    def sobe(self):
        if(self._andar_atual < self._total_andares):
            self._andar_atual+=1
            return True
        else:
            return False

    def desce(self):
        if(self._andar_atual > 0):
            self._andar_atual-=1
            return True
        else:
            return False

    @property
    def capacidade(self):
        return self._capacidade

    @capacidade.setter
    def capacidade(self, capacidade):
        if(capacidade>0):
            self._capacidade = capacidade
            return True
        else:
            return False

    @property
    def total_andares(self):
        return self._total_andares

    @total_andares.setter
    def total_andares(self, total_andares):
        if (total_andares > 0):
            self._total_andares = total_andares
            return True
        else:
            return False

    @property
    def quant_pessoas(self):
        return self._quant_pessoas

    @quant_pessoas.setter
    def quant_pessoas(self, quant_pessoas):
        if (quant_pessoas > -1):
            self._quant_pessoas = quant_pessoas
            return True
        else:
            return False

    @property
    def andar_atual(self):
        return self._andar_atual

    @andar_atual.setter
    def andar_atual(self, andar_atual):
        if (andar_atual > -1):
            self._andar_atual = andar_atual
            return True
        else:
            return False

