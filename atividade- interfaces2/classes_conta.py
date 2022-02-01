import abc
from datetime import datetime

class conta(abc.ABC):
    def __init__(self,numero,saldo,historico=[]):
        self._numero = numero
        self._saldo = saldo
        self._historico = historico

    @abc.abstractmethod
    def depositar(self):
        pass

    @abc.abstractmethod
    def sacar(self):
        pass

    @abc.abstractmethod
    def extrato(self):
        pass

    @property
    def saldo(self):
        return self._saldo


    @saldo.setter
    def saldo(self,saldo):
        if saldo > 0:
            self._saldo = saldo
            return 0
        else:
            return 1

    @property
    def historico(self):
        return self._historico


class Tributavel(abc.ABC):
    """
    Classe que contém operações de um objeto autenticável
    As subclasses concretas devem sobrescrever o método get_valor_imposto.
    """

    @abc.abstractmethod
    def get_valor_imposto(self):
        """"
        aplica taxa de imposto sobre um determinado valor do objeto
        """
        pass

class SeguroDeVida(Tributavel):
    def __init__(self, valor_mensal,valor_total):
        self._valor_mensal = valor_mensal
        self._valor_total = valor_total

    def get_valor_imposto(self):
        return self._valor_mensal * 0.02 + 10

    @property
    def valor_mensal(self):
        return self._valor_mensal

    @property
    def valor_total(self):
        return self._valor_total



class ContaCorrente(conta,Tributavel):

    data_abertura = datetime.today()
    tipo = "corrente"

    def __init__(self, numero,saldo, limite,historico = []):
        super().__init__( numero, saldo, historico)
        self._limite = limite

    def depositar(self,valor):

        if(valor>0):
            self.saldo += valor - 0.10
            self.historico.append(f"Na data {datetime.today()} \nFez um deposito de {valor}R$")

            return True
        else:
            return False

    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor

            self.historico.append(f" Na data {datetime.today()} \n fez um saque de {valor}R$")

            return True
        else:
            return False

    def extrato(self):
        print(f"saldo: {self.saldo}\n")

    def get_valor_imposto(self):
        return self.saldo * 0.01

    def imprimir_historico(self):
        print(f"\nData de abertura da conta: {ContaCorrente.data_abertura}")
        print("\nHistorico de operações da conta: ")

        if(len(self.historico) != 0):
            for i in self.historico:
                print(i)
        else:
            print("\n Nao foi feita nenhuma operacao nesta conta\n")

    def transferir(self, conta, valor):

        if (valor <= self.saldo):
            self.saldo -= valor
            conta.deposita(valor)
            self.historico.append(f" Na data {datetime.today()} \n fez uma trasferencia de {valor}R$")

            return True
        else:
            return False


class ContaPoupanca(conta):
    data_abertura = datetime.today()
    tipo = "poupanca"

    def depositar(self,valor):

        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Na data {datetime.today()} \nFez um deposito de {valor}R$")
            return True
        else:
            return False

    def sacar(self,valor):

        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f" Na data {datetime.today()} \n fez um saque de {valor}R$")

            return True
        else:
            return False

    def extrato(self):
        print(f"saldo: {self.saldo}\n")

    def imprimir_historico(self):
        print(f"\nData de abertura da conta: {ContaPoupanca.data_abertura}")
        print("\nHistorico de operações da conta: ")

        if (len(self.historico) != 0):
            for i in self.historico:
                print(i)
        else:
            print("\n Nao foi feita nenhuma operacao nesta conta\n")

    def transferir(self, conta, valor):

        if (valor <= self.saldo):
            self.saldo -= valor
            conta.deposita(valor)
            self.historico.append(f" Na data {datetime.today()} \n fez uma trasferencia de {valor}R$")

            return True
        else:
            return False


class Tributacao:
    historico = []
    qunt_tributacao = 0

    def cobrar_tributacao(self,imposto):
        total = imposto

        Tributacao.qunt_tributacao += 1
        Tributacao.historico.append(f"{Tributacao.qunt_tributacao} Tributacao: {total}")

        return total

    def imprimir_historico(self):
        for i in Tributacao.historico:
            print(i)
