from datetime import datetime

def depositar(valor, saldo, extrato):

    """
    Função para depositar um valor solicitado pelo usuário
    Returns:
        saldo : adiciona o valor solicitado na conta
        extrato: adiciona uma linha no histórico do extrato
    """

    if valor <= 0:
        print("\nDepósito inválido. Por gentileza digite valores positivos.") 
    
    else: 
        saldo += valor
        extrato += f"\n + R$ {valor:.2f}\t {registrar_data()}\t" # adiciona uma linha no histórico do extrato
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
    
    return saldo, extrato



def sacar(valor, saldo, /, limite_valor_saque, *,limite_saques_diario,extrato):

    """Realiza o saque solicitado pelo usuário desde que atenda as condições e regras

    Returns:
        saldo : subtrai valor solicitado do saldo na conta
        extrato : adiciona uma linha no histórico do extrato
        limite_saques_diario : subtrai 1 para cada saque realizado
    """


    if limite_saques_diario <= 0:
        print("\nOperação Recusada! Limite de número de saques diário atingido") 
    

    elif valor <= 0:
        print("\nOperação Recusada! Por gentileza, verifique o valor inserido e tente novamente.")
       

    elif valor > saldo:
        print("\nOperação Recusada! Não há saldo suficiente disponível.")

        
    elif valor > limite_valor_saque:
        print("\nOperação Recusada! Saque solicitado ultrapassa o limite permitido.")
        

    else:
        limite_saques_diario -= 1
        saldo -= valor
        extrato += f"\n - R$ {valor:.2f}\t {registrar_data()}\t" # adiciona uma linha no histórico do extrato
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
    
    return saldo, extrato, limite_saques_diario



def registros_extrato(saldo, /, *, extrato):

    print()
    print(" Extrato ".center(50,"="))
    print()
    print(extrato)
    print(f"\n\n\nSaldo atual: R$ {saldo:.2f}\t {registrar_data()}")
    return extrato



def registrar_data():
    
    """Registra as movimentações bancárias no padrão pt-br

    Returns:
        registro : dia/mês/ano Hora:Minuto:Segundo
    """

    padrao_ptbr = "%d/%m/%Y %H:%M:%S"
    registro = datetime.now().strftime(padrao_ptbr)
    return registro

def criar_usuario(lista_usuarios,cpf):

    nome = input("Informe o nome completo: ").title()
    
    print("\nInfomr a data de nascimento: ")
    dia = int(input("Dia: "))
    mes = int(input("Mês (número): "))
    ano = int(input("Ano: "))

    data_nascimento = f"{dia}/{mes}/{ano}"

    print("\nInforme o endereço: ")
    logradouro = input("Logradouro: ").title()
    numero = int(input("Número: "))
    bairro = input("Bairro: ").title()
    cidade = input("Cidade: ").title()
    estado = input("Sigla do Estado: ").upper()

    endereco = f"{logradouro} - {numero} - {bairro} - {cidade} - {estado}"

    novo_usuario = {"cpf":cpf,"data":data_nascimento,"nome":nome,"endereco":endereco}

    lista_usuarios.append(novo_usuario)

    return lista_usuarios


def verifica_usuario(lista_usuarios):

    cpf = int(input("Informe o CPF (somente números): "))

    usuario_existente = next((usuario for usuario in lista_usuarios if usuario["cpf"] == cpf), None)

    if usuario_existente:
        print("Usuário já cadastrado!")
        return usuario_existente
    
    else:
        opcao = input("Usuário não cadastrado! Gostaria de abrir uma conta ? [S/N]: ").upper()
        
        if opcao == "S":
            return criar_usuario(lista_usuarios,cpf)

        else:
            print("Operação cancelada")
            return None



def verifica_conta(lista_usuarios, lista_contas):

    cpf = int(input("Informe o CPF (somente números): "))

    # Verifica se o usuário existe
    usuario_existente = next((usuario for usuario in lista_usuarios if usuario["cpf"] == cpf), None)

    
    if not usuario_existente:
        
        opcao = input("CPF informado não possui cadastro. Deseja criar ? [S/N]").upper()

        if opcao == "S":
            usuario_existente = criar_usuario(lista_usuarios,cpf)

        elif opcao == "N":
            print("Operação Encerrada.")


    # Verifica se o CPF já tem alguma conta
    contas_existentes = [conta for conta in lista_contas if conta[2] == cpf]

    if contas_existentes:

        opcao = input("CPF informado já possui uma conta, deseja criar outra ? [S/N]")
        if opcao == "S":
            criar_conta(lista_contas= lista_contas, cpf=cpf, contas=contas)

        else:
            print("Operação Encerrada")
    
    else:
        criar_conta(lista_contas=lista_contas, cpf=cpf, contas=contas)
        print("Conta criada com sucesso!")


def criar_conta(lista_contas, cpf, contas):

    global AGENCIA
    contas = len(contas) + 1
    nova_conta = [AGENCIA, contas, cpf]

    lista_contas.append(nova_conta)

    return lista_contas, contas


saldo = 0
extrato = ""
numero_saques = 0
lista_usuarios = []
lista_contas = []
contas = []

LIMITE_VALOR_SAQUE = 500
LIMITE_SAQUES_DIARIOS = 3
AGENCIA = "0001"


while True:


    menu = """

==================================================

Selecione a operação desejada: 

[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova Conta
[lc] Listar Contas
[nu] Novo Usuário
[lu] Listar Usuários
[q] Sair

=> """

    opcao = input(menu).lower()

    # Realiza o depósito
    if opcao == "d":
        deposito = float(input("\nDigite o valor a ser depositado: R$ "))

        saldo, extrato = depositar(valor= deposito,
                                   saldo= saldo,
                                   extrato= extrato)
        

    # Realiza o saque
    elif opcao == "s":
        saque = float(input("\nDigite o valor a ser sacado: R$ "))

        saldo, extrato, LIMITE_SAQUES_DIARIOS = sacar(saque, 
                                                      saldo, 
                                                      limite_valor_saque= LIMITE_VALOR_SAQUE,
                                                      limite_saques_diario= LIMITE_SAQUES_DIARIOS,
                                                      extrato= extrato)
                                                      
        
    # Mostra o extrato bancário
    elif opcao == "e":
        registros_extrato(saldo, extrato=extrato)

    # Verifica se o usuário existe e da a opção de criar um novo
    elif opcao == "nu":
        verifica_usuario(lista_usuarios=lista_usuarios)

    # Lista os usuários existentes
    elif opcao == 'lu':
        print(lista_usuarios)

    # Lista as contas existentes
    elif opcao == "lc":
        print(lista_contas)
    
    # Cria uma nova conta
    elif opcao == "nc":
        verifica_conta(lista_usuarios = lista_usuarios, lista_contas= lista_contas)

    # Encerra o programa
    elif opcao == "q":
        print("\nEncerrando...") 
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")
