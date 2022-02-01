class produto:

    def __init__(self,cod_produto,nome_produto,tipo,marca,preco,quantidade):

        self._cod_produto = cod_produto
        self._nome_produto = nome_produto
        self._tipo = tipo
        self._marca = marca
        self._preco = preco
        self._quantidade = quantidade

    def imprimir_dados(self):
        print("---" * 30)
        print("Dados Produto: ")
        print(f" codigo: {self._cod_produto}")
        print(f" nome: {self._nome_produto}")
        print(f" tipo: {self._tipo}")
        print(f" marca: {self._marca}")
        print(f" preco: R$ {self._preco:.2f}")
        print(f" quantidade em estoque: {self._quantidade}\n")


    @property
    def cod_produto(self):
        return self._cod_produto

    @property
    def nome_produto(self):
        return self._nome_produto

    @property
    def tipo(self):
        return self._tipo

    @property
    def marca(self):
        return self._marca

    @property
    def preco(self):
        return self._preco

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quant):
        if quant >= 0:
            self._quantidade = quant
            return True
        else:
            return False


