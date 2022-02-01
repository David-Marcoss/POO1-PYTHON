class conta:
    def __init__(self,cliente,cod,saldo):
        self.cliente = cliente
        self.cod = cod
        self.saldo = saldo
        self.limite = 50000
        self.historico = historico()

    def deposita(self,saldo):
        self.saldo+= saldo
        print("deposito concluido!")
        print(f"saldo atual:{self.saldo} R$")

    def sacar(self,saldo):
        self.h = historico()
        if(saldo>self.saldo):
            print("nao é possivel sacar este valor!")
        else:
            self.saldo-=saldo
            self.historico.operacoes.append(f'saque de {saldo} feito com sucesso')
            print("saque feito com sucesso!")
            print(f"saldo atual: {self.saldo} R$")
    def extrato(self):
        self.cliente.imprimir()
        print(f"Saldo Atual : {self.saldo} R$")

    def mostrar_historico(self):
        self.historico.imprimir_historico()

    def atualiza(self,taxa):
        self.saldo += self.saldo * taxa

    def __str__(self):
        print("__" * 20)
        print("DADOS DA CONTA:")
        print("__"*20)
        print(f"codigo da conta : {self.cod}")
        print(f"saldo: {self.saldo}")
        self.cliente.imprimir()
        print(f"limite: {self.limite}")
        print(f"historico: {self.historico.imprimir_historico()}")
        print("__" * 20)


class ContaCorrente(conta):
    def atualiza(self,taxa):
        self.saldo += self.saldo * taxa * 2

    def deposita(self,valor):
        self.saldo += valor - 0.10

class ContaPoupanca(conta):
    def atualiza(self,taxa):
        self.saldo += self.saldo * taxa * 3

class AtualizadorDeContas:

    def __init__(self,selic,saldo_total= 0):
        self.selic = selic
        self.saldo_total = saldo_total

    def roda(self,conta):
        print(f"\nSaldo anterior: {conta.saldo}")
        conta.saldo += conta.saldo * self.selic
        self.saldo_total+= conta.saldo
        print(f"saldo final: {conta.saldo}\n")




class cliente:
    def __init__(self,nome,sobremome,cpf):
        self.nome = nome
        self.sobrenome = sobremome
        self.cpf = cpf

    def imprimir(self):
        print(f"nome:{self.nome}\nsobrenome: {self.sobrenome}\ncpf: {self.cpf}")

from datetime import datetime

class historico:
    def __init__(self):
        self.data = datetime.today()
        self.operacoes = []

    def imprimir_historico(self):
         print(self.data)
         for i in self.operacoes:
             print(i)

