from entidades.cliente import Cliente
from entidades.conta import Conta
    
CLIENTES = []
CONTAS = []

def chamar_menu():
    print("""============ Menu Bancário ============
1. Cadastrar Cliente
2. Cadastrar Conta
3. Realizar Movimentação
4. Exibir Clientes
5. Exibir Contas
6. Sair 
====================================\n""")

def cadastro_cliente():
    print("\n.....Iniciando cadastro de Cliente.....")
    print("====================================\n")
    nome_cli = input("Digite o nome do cliente: ")
    cpf = input("Digite o cpf do cliente: ")
    print("\n.....Fim do cadastro de cliente.....")
    print("====================================\n")

    return Cliente(nome_cli, cpf)
    
def validar_cpf_cliente(cpf_cli):
    for cliente in CLIENTES:
        if cliente.cpf == cpf_cli:
            return cliente
    return None

def cadastro_conta():
    i = 1
    print("\n.....Iniciando cadastro de Conta.....")
    print("====================================\n")
    tipo = input(f"Conta de id {i}\nDigite o tipo da conta: ")
    cpf_cli = input("Digite o CPF do cliente: ")
    
    cli_validado = validar_cpf_cliente(cpf_cli)
    if cli_validado == None:
        print("Cliente não encontrado na base")
        return
    
    conta = Conta(i, cli_validado, tipo)
    cli_validado.conta = conta
    i++1
    print("Cliente encontrado")
    print("\n.....Fim do cadastro de Conta.....")
    print("====================================\n")
    return conta
    
def movimentacao():
    # TODO
    ...



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
                print("Movimentação")
                
            case 4: # Exibir Clientes
                print("============ Exibindo clientes ============")
                for cliente in CLIENTES:
                    print(cliente)
            case 5: # Exibir Contas
                print("============ Exibindo contas ============")
                for conta in CONTAS:
                    print(conta)









main()