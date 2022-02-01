from random import randint

def sorteia():
    bilhete = []
    bilhete.append(randint(1,200))
    num = []
    for i in range(1,13):
        num.append(randint(1,3))

    bilhete.append(num)

    return bilhete

def acertos(gabarito,cartao):
    cont = 0
    for i in range(0,len(gabarito)):
        if(gabarito[i]==cartao[i]):
            cont+=1

    return cont

def imprimir(cartao):
    print('***'*30)
    print(f' numero do bilhete:{cartao[0]}\n valores apostados:{cartao[1]}\n numero de acertos:{acertos(cartao[1], gabarito[1])}\n')
    if(acertos(cartao[1], gabarito[1])==13):
        print('GANHADOR!!!!')
        print('***' * 30)


gabarito = sorteia()
cartao1 = sorteia()
cartao2 = sorteia()
cartao3 = sorteia()

print('***' * 30)
print(f'gabarito: {gabarito[1]}')
imprimir(cartao1)
imprimir(cartao2)
imprimir(cartao3)




