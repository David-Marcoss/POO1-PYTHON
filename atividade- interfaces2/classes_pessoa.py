class pessoa:
    def __init__(self, nome, cpf, data_nascimento):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def data_nascimento(self):
        return self._data_nascimento


class funcionario(pessoa):

    def __init__(self,nome, cpf, data_nascimento,salario):
        super(funcionario, self).__init__(nome, cpf, data_nascimento)
        self._salario = salario

    def imprimir_dados(self):
        print("\nDados Funcionario: ")
        print(f" nome: {self._nome}")
        print(f" cpf: {self.cpf}")
        print(f" data de nascimento: {self._data_nascimento}")
        print(f" salrio: {self._salario}\n")


class cliente(pessoa):

    def __init__(self, nome, cpf, data_nascimento, profissao,renda):
        super(cliente, self).__init__(nome, cpf, data_nascimento)
        self._profissao = profissao
        self._renda = renda
        self._contas = []
        self._seguro_vida = []

    def imprimir_dados(self):
        print("\nDados Cliente: ")
        print(f" nome: {self._nome}")
        print(f" cpf: {self.cpf}")
        print(f" data de nascimento: {self._data_nascimento}")
        print(f" profissao: {self._profissao}")
        print(f" renda: {self._renda}\n")

    def criar_conta(self,conta):
        self._contas.append(conta)

    def criar_seguro(self, seguro):
        self._seguro_vida.append(seguro)

    @property
    def contas(self):
        return self._contas

    @property
    def seguro_vida(self):
        return self._seguro_vida

