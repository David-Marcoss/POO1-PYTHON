import abc

class conta(abc.ABC):
    def __init__(self,numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    @abc.abstractmethod
    def deposita(self):
        pass

    @abc.abstractmethod
    def sacar(self):
        pass

    @abc.abstractmethod
    def extrato(self):
        pass

    @abc.abstractmethod
    def atualiza(self):
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
    def titular(self):
        return self._titular


class ContaCorrente(conta):

    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        super().__init__( numero, titular, saldo, limite)
        self.tipo = type(self).__name__

    def deposita(self,valor):
        self.saldo += valor - 0.10

    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return 0
        else:
            return 1

    def extrato(self):
        print(f"saldo: {self.saldo}\n")

    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 2

    def __str__(self):
        return "tipo da conta: " + self.tipo + "\n" + "Titular: " + self.titular + "\n" + "Saldo:" + str(self.saldo) + "\n"


class ContaPoupanca(conta):

    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        super().__init__(numero, titular, saldo, limite)
        self.tipo = type(self).__name__

    def deposita(self,valor):
        self.saldo += valor

    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return 0
        else:
            return 1

    def extrato(self):
        print(f"saldo: {self.saldo}\n")

    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 3

    def __str__(self):
        return "tipo da conta: " + self.tipo + "\n" + "Titular: " + self.titular + "\n" + "Saldo:" + str(self.saldo) + "\n"


class ContaInvestimento(conta):
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        super().__init__(numero, titular, saldo, limite)
        self.tipo = type(self).__name__

    def deposita(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return 0
        else:
            return 1

    def extrato(self):
        print(f"saldo: {self.saldo}\n")

    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 5

    def __str__(self):
        return "tipo da conta: " + self.tipo + "\n" + "Titular: " + self.titular + "\n"+ "Saldo:" + str(self.saldo)+ "\n"






