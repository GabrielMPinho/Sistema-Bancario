from entidades.cliente import Cliente
from entidades.conta import Conta
import time
import os
    
CLIENTES = []
CONTAS = []
ID_CONTA = 1

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def chamar_menu():
    limpar_terminal()
    print("""============ Menu Bancário ============
1. Cadastrar Cliente
2. Cadastrar Conta
3. Realizar Movimentação
4. Exibir Clientes
5. Exibir Contas
6. Sair 
====================================\n""")

def cadastro_cliente():
    limpar_terminal()
    print("\n.....Iniciando cadastro de Cliente.....")
    print("====================================\n")
    time.sleep(1)
    nome_cli = input("Digite o nome do cliente: ")
    time.sleep(1)
    cpf = input("Digite o cpf do cliente: ")
    time.sleep(1)

    print("\n.....Fim do cadastro de cliente.....")
    print("====================================\n")
    time.sleep(2)

    return Cliente(nome_cli, cpf)
    
def validar_cpf_cliente(cpf_cli):
    for cliente in CLIENTES:
        if cliente.cpf == cpf_cli:
            return cliente
    return None

def cadastro_conta():
    global ID_CONTA
    limpar_terminal()
    print("\n.....Iniciando cadastro de Conta.....")
    print("====================================\n")
    time.sleep(1)

    tipo = input(f"Conta de id {ID_CONTA}\nDigite o tipo da conta: ")
    time.sleep(1)
    cpf_cli = input("Digite o CPF do cliente: ")
    time.sleep(1)
    cli_validado = validar_cpf_cliente(cpf_cli)
    if cli_validado == None:
        print("Cliente não encontrado na base")
        return
    
    conta = Conta(ID_CONTA, cli_validado, tipo)
    cli_validado.conta = conta
    ID_CONTA+=1
    print("Cliente encontrado")
    time.sleep(1)
    print("\n.....Fim do cadastro de Conta.....")
    print("====================================\n")
    time.sleep(2)
    return conta
    
def movimentacao(id_conta, valor):
    global CONTAS
    for conta in CONTAS:
        if conta.id == id_conta:
            conta.saldo += valor
            if valor > 0:
                print(f"Conta de id {id_conta} adicionada R$ {valor}")
                time.sleep(1)
                print(f"Saldo atual: {conta.saldo}")
                time.sleep(2)
            elif valor < 0:
                print(f"Conta de id {id_conta} retirado R$ {valor}")
                time.sleep(1)
                print(f"Saldo atual: {conta.saldo}")
                time.sleep(2)
            else:
                print("Valor de movimentação = 0")
                time.sleep(1)
                print(f"Saldo atual: {conta.saldo}")
                time.sleep(2)
        else:
            print("ID inválido")
    






def main():
    escolha = 0
    while escolha != 6:
        chamar_menu()
        escolha = int(input("Selecione uma opção: "))
        match escolha:
            case 1: # Cadastro cliente
                cliente = cadastro_cliente()
                CLIENTES.append(cliente)
                
            case 2: # Cadastro Conta
                conta = cadastro_conta()
                CONTAS.append(conta)
                
            case 3: # Movimentação
                limpar_terminal()
                id = int(input("Digite o id da conta: "))
                time.sleep(1)
                valor = int(input("Digite o valor a ser movimentado: "))
                time.sleep(1)
                movimentacao(id, valor)
            case 4: # Exibir Clientes
                print("============ Exibindo clientes ============")
                time.sleep(1)
                for cliente in CLIENTES:
                    print(cliente)
                time.sleep(2)
            case 5: # Exibir Contas
                print("============ Exibindo contas ============")
                time.sleep(1)
                for conta in CONTAS:
                    print(conta)
                time.sleep(2)


main()