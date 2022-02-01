
import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color

def mostra(nome, idade, data):
    layout = [
        [sg.Text(f'dados cliente: ')],
        [sg.Text(f'nome: {nome} ')],
        [sg.Text(f'idade: {idade}')],
        [sg.Text(f'data: {data}')],
        [sg.Button('sair')],
    ]

    tela = sg.Window('cadrasto:', layout, size=(500, 500))

    event, values = tela.read()

def menu():
    layout = [
        [sg.Button('cadrastar cliente',size=(50,5))],
        [sg.Button('cadrastar funcionario',size=(50,5))],
        [sg.Button('cadrstar produto',size=(50,5))],
        [sg.Button('imprimir cliente',size=(50,5))],
        [sg.Button('sair', size=(50,5))],

    ]

    tela = sg.Window('cadrasto:', layout, size=(1000, 1000))

    event, values = tela.read()




layout = [
    [sg.Text('nome: '),sg.Input(),],
    [sg.Text('idade: '),sg.Input()],
    [sg.Text('Finalizar cadrastro: ')],
    [sg.Button('sim'), sg.Button('Nao')],
]

tela = sg.Window('cadrasto:',layout,size=(500,500))

event, values = tela.read()

L7 = []

L7.append("nome: david")
L7.append("idade: 20")
L7.append("data de nascimento: 14/03/2001")

menu()
mostra("david","20", "14/03/2001")






