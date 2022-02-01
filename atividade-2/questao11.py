def media(alunos):
    nome = str(input("\ndigite o nome do aluno: "))
    flag = 0
    for k in alunos.keys():
        if(k == nome):
            M = (alunos[nome][0] + alunos[nome][1])/2
            flag = 1
    if flag == 0:
        print("aluno nao encontrado!")
    else:
        print(f"\nmedia do aluno {nome} : {M}")

    return M


alunos = {}

n=1
while(n>0):
    notas = []
    nome = str(input("digite o nome do aluno: "))
    notas.append(float(input("digite a primeira nota: ")))
    notas.append(float(input("digite a segunda nota: ")))
    alunos[nome] = notas

    n = int(input("\ndigite 1 para continuar e -1 para parar: "))

M = media(alunos)



