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



saldo = 0
extrato = ""
numero_saques = 0

LIMITE_VALOR_SAQUE = 500
LIMITE_SAQUES_DIARIOS = 3


while True:

    menu = """

==================================================

Selecione a operação desejada: 

[d] Depositar
[s] Sacar
[e] Extrato
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

    # Encerra o programa
    elif opcao == "q":
        print("\nEncerrando...") 
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")
