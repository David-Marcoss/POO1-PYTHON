def ler(corredores):
    voltas = []
    n = str(input("digite o nome do corredor: "))
    voltas.append(int(input("digite seu tempo na volta 1: ")))
    voltas.append(int(input("digite seu tempo na volta 2: ")))
    voltas.append(int(input("digite seu tempo na volta 3: ")))
    print("---" * 20)

    corredores[n] = voltas

def campeao(corredores):
    menor_t = 0
    menor_m = 0
    media_t = 0
    flag = 0
    nome_v1 = ''
    nome_v2 = ''

    for k in corredores.keys():
        if flag == 0:
            menor_t = corredores[k][0]

            for tempo in corredores[k]:
                media_t += tempo
                if (tempo < menor_t):
                    menor_t = tempo

            menor_m = media_t / 3
            nome_v1 = k
            nome_v2 = k
            flag = 1

        else:
            media_t = 0
            for tempo in corredores[k]:
                media_t+= tempo
                if(tempo < menor_t):
                    menor_t = tempo
                    nome_v1 = k

            media_t/=3
            if media_t < menor_m :
                menor_m = media_t
                nome_v2 = k

    print(f'corredor {nome_v1} fez a melhor volta com tempo de {menor_t} Sgs . ')
    print(f'corredor {nome_v2} foi o campeao com media de tempo de {menor_m} Sgs . ')




corredores = {}

for i in range(0,2):
    ler(corredores)

campeao(corredores)