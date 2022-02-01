import abc
from datetime import date

class pessoa(abc.ABC):

    def __init__(self, nome, cpf, telefone,data_nascimento):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._data_nascimento = data_nascimento
        self._data_de_cadrastro = date.today().strftime('%d/%m/%Y')

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def telefone(self):
        return self._telefone

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def data_de_cadrastro(self):
        return self._data_de_cadrastro

    @abc.abstractmethod
    def imprimir_dados(self):
        pass



class cliente(pessoa):

    def imprimir_dados(self):
        print("---" * 30)
        print("Dados Cliente: ")
        print(f" nome: {self.nome}")
        print(f" cpf: {self.cpf}")
        print(f" contato: {self.telefone}")
        print(f" data de nascimento: {self.data_nascimento}")
        print(f" data de cadrastro: {self.data_de_cadrastro}\n")



class funcionario(pessoa):

    def __init__(self, nome, cpf, telefone,data_nascimento,cod_indentificacao,salario):
        super().__init__(nome, cpf, telefone,data_nascimento)
        self._cod_indentificacao =cod_indentificacao
        self._salario = salario
        self._quant_vendas = 0

    def imprimir_dados(self):
        print("---" * 30)
        print("Dados Funcionario: ")
        print(f" codigo de indentificacao :{self._cod_indentificacao}")
        print(f" nome: {self.nome}")
        print(f" cpf: {self.cpf}")
        print(f" contato: {self.telefone}")
        print(f" data de nascimento: {self.data_nascimento}")
        print(f" data de contratacao: {self.data_de_cadrastro}")
        print(f" valor salario :R$ {self._salario:.2f}")

    def imprimir_quantidade_de_vendas(self):
        print(f" {self.nome} concluiu {self._quant_vendas} vendas")

    @property
    def cod_indentificacao(self):
        return self._cod_indentificacao

    @property
    def salario(self):
        return self._salario

    @property
    def quant_vendas(self):
        return self._quant_vendas

    @quant_vendas.setter
    def quant_vendas(self,valor):

        if valor >= 0:
            self._quant_vendas = valor
            return True
        else:
            return False



#interface altenticavel
class autentivcavel(abc.ABC):

    @abc.abstractmethod
    def autentica(self,cod_indentificacao,senha):
        pass


class gerente(funcionario):

    def __init__(self, nome, cpf, telefone, data_nascimento, cod_indentificacao, salario,senha):
        funcionario.__init__(self, nome, cpf, telefone, data_nascimento, cod_indentificacao, salario)
        self.senha = senha

    def autentica(self,senha,cod_indentificacao):
        if senha == self.senha and cod_indentificacao == self.cod_indentificacao:
            return True
        else:
            return False
