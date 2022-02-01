from math import sqrt
def inicia():
    num = []
    for i in range(1,101):
        num.append(i)

    return num

def media(num):
    media = 0
    for i in num:
        media+=i
    media = media/len(num)
    return media

def mediana(num):
    num.sort()
    if len(num) % 2== 0:
        i = len(num)//2
        mediana = (num[i]+num[i+1])/2
    else:
        i = len(num) // 2
        mediana = num[i]

    return mediana

def variancia(num,media):
    var = 0
    for i in num:
        var+= pow(i-media,2)
    var = var/len(num)
    return var

def desvio_padrao(num,media):
    dp = 0
    for i in num:
        dp+= pow(i-media,2)
    dp = sqrt(dp/len(num))

    return dp

num = inicia()

print(f'media: {media(num)}')
print(f'mediana: {mediana(num)}')
print(f'variancia: {variancia(num,mediana(num))}')
print(f'desvio padrao: {desvio_padrao(num,mediana(num))}')