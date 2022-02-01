from random import randint

def adivinha():
    tentativas = 1
    num = randint(0,100)
    while(tentativas < 11):

        print("*"*40)
        print("tentativa {}".format(tentativas))
        n = int(input("\nescolha um numero:"))

        if(n == num):
            print("\n","*" * 40)
            print("PARABENS VOCE ACERTOU!!!")
            print("*" * 40)
            return 1
        else:
            print("*" * 40)
            print("ERROU!!!")
            print("*" * 40)
            print("\n" * 4)
            tentativas+=1

    return 0
n = 1

while n == 1:
    print("JOGO DA ADIVINHAÇÂO:")

    n= adivinha()

    if n == 1:
        print("\n")
        n = int(input("digite 1 se deseja continuar ou 0 para sair: "))
        print("\n" * 6)
    else:
        break