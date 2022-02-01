class agenda:
    contador = 0
    def __init__(self):
        self.dic = {}
    def armazena(self,nome,idade,altura):
        self.dic[nome] = [idade,altura]
        agenda.contador+=1

    def remove(self,nome):
        if nome in self.dic.keys():
            self.dic.pop(nome)
            agenda.contador-=1
            return True
        else:
            return False

    def imprimiragenda(self):
        for k,v in self.dic.items():
            print(f"\nnome: {k}\nidade: {v[0]}\naltura:{v[1]}")

    def busca(self,nome):
        if nome in self.dic.keys():
            return True
        else:
            return False



    def imprimirpessoa(self,nome):
        if nome in self.dic.keys():
            print(f"\nnome: {nome}\nidade: {self.dic[nome][0]}\naltura:{self.dic[nome][1]}")
            return True
        else:
            return False


def menu():
    print("\n1-armazena Pessoa")
    print("2-remove Pessoa")
    print("3-busca Pessoa")
    print("4-imprimeAgenda")
    print("5-imprime Pessoa")
    print("6-sair ")
    op = int(input("\ndigite a opcao: "))
    return op

def ler():
    nome = str(input("digite o nome: "))
    idade = int(input("digite sua idade: "))
    altura = float(input("digite sua altura: "))

    return nome,idade,altura

c = agenda()
op = menu()
while(op<6):

    if(op == 1):
        if(agenda.contador<= 10):
            nome, idade, altura = ler()
            c.armazena(nome,idade,altura)
            print("Pessoa adicionada com sucesso!")
        else:
            print("agenda lotada!")

    elif(op == 2):
        nome = str(input("digite o nome da pessoa: "))
        if(c.remove(nome)):
            print(f"{nome} removido da agenda com sucesso")
        else:
            print(f"{nome} nao encontrado na agenda")

    elif (op == 3):
        nome = str(input("digite o nome da pessoa: "))
        if (c.busca(nome)):
            print(f"pessoa encontrada na agenda com sucesso")
        else:
            print(f"pessoa nao encontrada na agenda")
    elif(op == 4):
        if(agenda.contador > 0):
            c.imprimiragenda()
        else:
            print("Erro: agenda vazia")

    elif (op == 5):
        nome = str(input("digite o nome da pessoa: "))
        if (not c.imprimirpessoa(nome)):
            print(f"{nome} nao encontrado na agenda")

    op = menu()