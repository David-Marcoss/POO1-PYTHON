
def contatos():
    agenda = []
    for i in range(0,10):
        dados = {}
        dados['nome'] = str(input('nome:'))
        dados['endereco'] = str(input('endereco:'))
        dados['cep'] = str(input('CEP:'))
        dados['Bairro'] = str(input('Bairro:'))
        dados['telefone'] = int(input('telefone:'))
        print('\n')
        agenda.append(dados)
    return agenda

def imprime(agenda):
    for i in range(len(agenda)-1,-1,-1):
        print('--' * 30)
        for k,v in agenda[i].items():
            print(f'{k} : {v}')



agenda = contatos()
imprime(agenda)
