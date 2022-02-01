preco = 5.0
quant = 120
max_lucro = 0

while(preco>1):
    lucro = preco*quant-200

    print('preco do ingreco = {:.2f}, quantidade = {}, lucro = {:.2f}'.format(preco,quant,lucro))
    if( lucro > max_lucro):
        max_lucro = lucro
        aux1 = preco
        aux2 = quant
    preco-=0.50
    quant+=26


print('\nlucro maximo = {:.2f}\npreco do ingreco = {:.2f}\nquantidade vendida = {}'.format(max_lucro,aux1,aux2))