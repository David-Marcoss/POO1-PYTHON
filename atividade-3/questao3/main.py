from classes import elevador
from time import sleep
def menu():
    print("\n1-inicializa")
    print("2-entra")
    print("3-sai")
    print("4-Sobe")
    print("5-Desce")
    print("6-sair ")
    op = int(input("\ndigite a opcao: "))
    return op

def ler():
    capacidade = int(input("digite a capacidade do elevador: "))
    t_andares = int(input("digite o total de andares: "))

    return capacidade,t_andares


op = menu()

while(op<6):

    if(op == 1):
        capacidade,t_andares = ler()
        elevador = elevador(capacidade,t_andares)

    elif(op == 2):
        if(elevador.entra()):
            print("Uma pessoa entrou no elevador!")
        else:
            print("o elevador esta lotado")
    elif (op == 3):
        if (elevador.sai()):
            print("Uma pessoa saiu do elevador!")
        else:
            print("o elevador esta vazio")

    elif(op == 4):
        if (elevador.sobe()):
            print("subindo...")
            sleep(1)
            print(f"elevador subiu um andar! O elevador esta no {elevador.andar_atual} andar")
        else:
            print("Nao e possivel subir o elevador  esta no ultimo andar!")

    elif (op == 5):
        if (elevador.desce()):
            print("descendo...")
            sleep(1)
            print(f"elevador deceu um andar! O elevador esta no {elevador.andar_atual} andar")
        else:
            print("Nao e possivel descer, o esta elevador no Terreo!")

    op = menu()