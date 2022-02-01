from classes import turma

def menu():
    print("\n1-inserir aluno")
    print("2- calcular a media de um aluno")
    print("3- quanto o aluno precisa tirar na prova final")
    print("4- encerrar turma")
    print("5- Listar alunos ")
    print("6-sair ")
    op = int(input("\ndigite a opcao: "))
    return op

def ler():
    matricula = int(input("digite a matricula: "))
    nome = str(input("digite o nome: "))
    notas = []

    print("digite as notas do aluno: ")

    for i in range(0,3):
        N = float(input(f" Nota {i+1}: "))
        notas.append(N)

    return matricula,nome,notas


Turma = turma()

op = menu()
flag = 0

while(op<6):

    if(op == 1):
        matricula, nome, notas = ler()
        if(Turma.insere_aluno(matricula, nome, notas)):
            print("\naluno inserido na turma!\n")
        else:
            print("\nNao e possivel inserir aluno!! Esta matricula ja existe")

    if (op == 2):
        mat = int(input("digite a matricula do aluno:"))
        if(Turma.busca(mat)):
            media = Turma.media(Turma.turma[mat].notas)
            print(f"\nmedia do aluno {Turma.turma[mat].nome}: {media}\n")
        else:
            print("\naluno nao existe!\n")

    if (op == 3):
        mat = int(input("digite a matricula do aluno:"))
        if (Turma.busca(mat)):
            N = Turma.final(Turma.turma[mat])
            if(N>0):
                print(f"\nO aluno {Turma.turma[mat].nome}: presisa tirar nota {N} para passar na final\n")
            else:
                print("\nEste aluno nao foi para a final!")
        else:
            print("\naluno nao existe!")

    if (op == 4):

        if(Turma.tem_aluno()):
            flag = 1
            Turma.encerramento_turma()
            print("\nOperação concluida!")
        else:
            print("\nNao possui alunos inseridos na turma!")
    if (op == 5):
        if(Turma.tem_aluno()):
            if(flag==0):
                Turma.encerramento_turma()
                flag = 1
                Turma.listagem_alunos()
            else:
                Turma.listagem_alunos()
        else:
            print("\nNao possui alunos inseridos na turma!")

    op = menu()