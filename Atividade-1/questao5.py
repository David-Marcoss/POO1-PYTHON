def fatorial(n):
    fat =1
    for i in range(2,n+1):
        fat*= i

    return fat

n = int(input('digite um valor: '))
p = int(input('digite um valor: '))

A = fatorial(n)/fatorial(n-p)
C = fatorial(n)/(fatorial(p)*fatorial(n-p))

print('Arranjo = {}'.format(A))
print('conbinação = {}'.format(C))

