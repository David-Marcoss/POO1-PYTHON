class aluno:
    def __init__(self,matricula,nome,notas):
        self.matricula = matricula
        self.nome = nome
        self.notas = notas

    def imprimir(self):
        print(f"\nmatricula: {self.matricula}")
        print(f"nome: {self.nome}")
        print(f"notas: {self.notas}\n")

class turma:
    def __init__(self):
        self.turma = {}

    def insere_aluno(self,matricula,nome,notas):
        if(self.busca(matricula)):
            return False
        else:
            p = aluno(matricula, nome, notas)
            self.turma[matricula] = p
            return True

    def imprimir_alunos(self):
        for v in self.turma.values():
            v.imprimir()



    def media(self,notas):   #recebe as medias de um aluno inserido no dicionario

        media = (notas[0]*2 + notas[1]*3 + notas[2] * 5)/(2+3+5)
        return media

    def final(self,aluno): #recebe um aluno inserido no dicionario
        F = 0
        M = self.media(aluno.notas)
        if(M < 7):
            F = 14-M

        return F

    def encerramento_turma(self):
        self.L_alunos = []
        if( self.tem_aluno()):
            for v in self.turma.values():
                aux = []
                m = self.media(v.notas)
                aux.append(v.nome)
                aux.append(m)
                self.L_alunos.append(aux)
            return True
        return False

    def listagem_alunos(self):
        if (self.tem_aluno()):
            for i in self.L_alunos:
                print(f"\nnome do aluno: {i[0]}")
                print(f"media: {i[1]}\n")
            return True
        return False

    def busca(self,mat):
        if mat in self.turma.keys():
            return True
        else:
            return False

    def tem_aluno(self):
        if len(self.turma) > 0:
            return True
        return False