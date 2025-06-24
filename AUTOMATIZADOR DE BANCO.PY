MENU = """
[D] Depositar
[S] Sacar
[E] Extrato 
[Q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

print("======= BEM VINDO AO LIMAS BANK =======")

while True:
    print("======== MENU BANCÁRIO ========")
    print(MENU)

    opcao = input("SELECIONE UMA OPÇÃO: ").strip().upper()

    if opcao == "D":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.\n")
        else:
            print("Valor inválido para depósito.\n")

    elif opcao == "S":
        valor = float(input("Informe o valor do saque desejado: "))
  
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Saldo insuficiente.")

        elif excedeu_limite:
            print("O valor excede o limite por saque.")

        elif excedeu_saques:
            print("Limite de saques diários atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saldo atual: R${saldo:.2f}")
    
    elif opcao == "E":
        print("====Extrato====\n")
        if extrato:
                print(extrato)
        else:
                print("Não foram Realizadas nenhuma Transação ")
                print(f"\n Saldo: R${saldo:.2f}")
        print("================")
    
    elif opcao == "Q":
         break
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
