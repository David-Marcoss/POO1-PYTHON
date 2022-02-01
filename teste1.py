""""
class conta:
    def __init__(self,cliente):
        self.cliente = cliente
        self.cod = input("digite o codigo:")
        self.saldo = float(input("digite o saldo:"))
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

c1 = cliente("david","marcos","0923.323.33")
c = conta(c1)
c.sacar(100)
c.sacar(250)
c.mostrar_historico()
"""
s