from datetime import date

class pessoa:
    def __init__(self,nome,data,altura):
        self._nome = nome
        self._data = data
        self._altura = altura

    def imprimir_dados(self):

        print(f"nome:{self._nome}\ndata de nacimento:{self._data}\naltura:{self._altura}\nidade: {self.idade()}\n")

    def idade(self):
        dt = self.data.split("/")
        if( (len(dt[0]) <3 ) and (len(dt[1]) <3 ) and (len(dt[2]) <5)):

            ano_atual = date.today()
            ano = int(dt[2])
            idade1 = ano_atual.year - ano
            return idade1
        else:
            print("Erro: nao foi possivel calcular idade")
            return -1


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        dt = data.split("/")
        if( (len(dt[0]) <2 ) and (len(dt[1]) <2 ) and (len(dt[2]) <4)):
            self.data.copy(data)
        else:
            print("Erro! formato da data de nacimemto errado")

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if(altura>0):
            self._altura = altura
        else:
            print("Erro: altura não pode ser negatva")



p1 = pessoa("david","14/03/2001",1.70)
p2 = pessoa("carlos","14/03/1991",1.70)


p1.imprimir_dados()
p2.imprimir_dados()


p1.idade()