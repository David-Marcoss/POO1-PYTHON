from classes import televisao,controleremoto

def menu():
    print("\n1-aumentar volume")
    print("2- diminuir volume")
    print("3- passar canal")
    print("4- voltar canal")
    print("5- trocar canal")
    print("6- ver canal atual")
    print("7- ver volume atual")
    print("8-sair ")
    op = int(input("\ndigite a opcao: "))
    return op


op = menu()
controle = controleremoto()

while(op<8):

    if(op == 1):
        if(controle.aumentar()):
            print(f"\nvolume aumentado! volume atual: {controle.vervolume()}")
        else:
            print("\no volume ja esta no maximo!!")

    elif(op == 2):
        if (controle.diminuir()):
            print(f"\nvolume diminuido! volume atual: {controle.vervolume()}")
        else:
            print("\no volume ja esta no mais baixo!!")

    elif (op == 3):
        if (controle.passarcanal()):
            print(f"\ncanal passado! canal atual: canal {controle.vercanal()}")
        else:
            print("\nnao é possivel passar canal!!")

    elif(op == 4):

        if (controle.voltarcanal()):
            print(f"\ncanal voltado! canal atual: canal {controle.vercanal()}")
        else:
            print("\nnao é possivel voltar canal!!")

    elif (op == 5):
        canal = int(input("escolha o canal:"))
        if (controle.trocarcanal(canal)):
            print(f"\ncanal trocado! canal atual: canal {controle.vercanal()}")
        else:
            print("\nCanal escolhido nao existe!")

    elif (op == 6):
        print(f"\ncanal atual: canal {controle.vercanal()}")

    elif (op == 7):
        print(f"\nvolume atual: {controle.vervolume()}")

    op = menu()