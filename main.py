import os

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

listaDeCarros = []
listaDeMotoristas = []
listaDeProprietarios = []

class Carro:
    def __init__(self, marca, nome, ano, cor, placa, renavam): #esse Carro tem um Proprietario
        self.marca = marca
        self.nome = nome
        self.ano = ano
        self.cor = cor
        self.placa = placa
        self.renavam = renavam

def cadastrarCarro():
    marcaCarro = input("Digite a MONTADORA do Carro: ")
    nomeCarro = input("Digite o NOME do Carro: ")
    anoCarro = input("Digite o ANO do Carro: ")
    corCarro = input("Digite a COR do Carro: ")
    placaCarro = input("Digite A PLACA no formato : XXX-0000: ")
    renavamCarro = input("Digite O RENAVAM do Carro: ")
    novoCarro = Carro(marcaCarro, nomeCarro, anoCarro, corCarro,placaCarro, renavamCarro)
    listaDeCarros.append(novoCarro)

def listarCarros():
    for x in listaDeCarros:
        print()
        print(f'Marca: {x.marca} - Nome: {x.nome} - Cor: {x.cor} - Placa: {x.placa}')

class Motorista:
    def __init__(self, nome, cpf, cnh): #esse Motorista dirige um Carro
        self.nome = nome
        self.cpf = cpf
        self.cnh = cnh

def cadastrarMotorista():
    nomeMotorista = input("Digite o nome do motorista: ")
    cpfMotorista = input("Digite o CPF do motorista: ")
    cnhMotorista = input("Digite a CNH do motorista: ")
    novoMotorista = Motorista(nomeMotorista, cpfMotorista, cnhMotorista)
    listaDeMotoristas.append(novoMotorista)

def listarMotoristas():
    for x in listaDeProprietarios:
        print()
        print(f'Nome : {x.nome} - CPF: {x.cpf} - CNH: {x.cnh}')

class Proprietario:
    def __init__(self, nome, chavePix): # esse proprietario pode ter mais de um Carro
        self.nome = nome
        self.chavePix = chavePix

def cadastrarProprietario():
    nomeProprietario = input("Digite o nome do proprietário: ")
    chavePixProprietario = input("Digite a chave pix do proprietário: ")
    novoProprietario = Proprietario(nomeProprietario, chavePixProprietario)
    listaDeProprietarios.append(novoProprietario)

def listarProprietarios():
    for x in listaDeProprietarios:
        print()
        print(f'Nome : {x.nome} - Chave Pix : {x.chavePix}')

def menu():
    print('=' * 40)
    print('1- Cadastrar Novo Proprietário.')
    print()
    print('2- Listar Proprietários.')
    print()
    print('3- Cadastrar Novo Motorista.')
    print()
    print('4- Listar Motoristas.')
    print()
    print('5- Cadastrar Novo Carro.')
    print()
    print('6- Listar Carros.')
    print()
    entrada = int(input("DIGITE A OPÇÃO: "))
    if entrada == 1:
        cadastrarProprietario()
    elif entrada == 2:
        listarProprietarios()
    elif entrada == 3:
        cadastrarMotorista()
    elif entrada == 4:
        listarMotoristas()
    elif entrada == 5:
        cadastrarCarro()
    elif entrada == 6:
        listarCarros()
    else :
        print("entrada invalida!")

while True:
    limparTela()
    menu()
