def posicao(palavra,letra):

    for i in range(0,len(palavra)):
        if palavra[i] == letra:
            return i

    return -1


palavra = str(input("digite uma palavra: "))

while True:
    letra = str(input("digite uma letra para busca: "))
    if(len(letra)>1):
        print("erro!! A letra so deve possuir um caracter")
    else:
        break

posi = posicao(palavra,letra)

if(posi == -1):
    print("o caracter nao existe na palavra!!")
else:
    print("o caracter {} esta na posicao {} da palavra {}".format(letra,posi,palavra))
