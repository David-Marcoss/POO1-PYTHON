
class cliente:

    def __init__(self,cod,nome,saldo):
        self.cod = cod
        self.nome = nome
        self.saldo = saldo

    def saldo(self):
        print(f"codigo: {self.cod}\nnome: {self.nome}\nsaldo: {self.saldo}\n")

    def get_saldo(self,saldo):
          self.saldo = saldo

    def set_saldo(self, saldo):
        return self.saldo


c = cliente(1,"david",1000)

c.get_saldo(200)

c.saldo()
