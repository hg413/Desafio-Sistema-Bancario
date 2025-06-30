import textwrap

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente números): ").strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já cadastrado com este CPF!")
        return

    nome = input("Informe seu nome completo: ")
    data_de_nasc = input("Informe sua data de nascimento: ")
    endereco = input("Informe seu endereço (Logradouro, Nro - Bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_de_nasc": data_de_nasc,
        "cpf": cpf,
        "endereco": endereco
    })
    print("======= USUÁRIO CADASTRADO =======")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ").strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n ====CONTA CRIADA====")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n Usuário não encontrado, Programa encerrado")
    return  # corrigido: era 'break'

def listar_contas(contas):
    for conta in contas:
        linha = f"""\ 
        Agência:\t{conta["agencia"]}
        C/C:\t\t{conta["numero_conta"]}
        Titular:\t\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0008"

    saldo = 0
    extrato = ""
    limite = 500
    numero_saques = 0
    usuarios = []
    contas = []

    MENU = """
[D] Depositar
[S] Sacar
[E] Extrato
[G] Listar contas
[U] Criar Usuário
[F] Criar conta
[Q] Sair
"""

    print("======= BEM VINDO AO LIMAS BANK =======")

    while True:
        print(MENU)
        opcao = input("Selecione uma opção: ").strip().upper()

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
            excedeu_saques = numero_saques >= LIMITE_SAQUE  # corrigido para usar constante certa

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
                print(f"Saldo atual: R$ {saldo:.2f}")
            else:
                print("Valor inválido para saque.")

        elif opcao == "E":
            print("==== EXTRATO ====\n")
            print(extrato if extrato else "Não foram realizadas transações.")
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==================")

        elif opcao == "U":
            criar_usuario(usuarios)

        elif opcao == "F":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)  # corrigido: antes estava 'contas.append(contas)'

        elif opcao == "G":
            listar_contas(contas)

        elif opcao == "Q":
            break

        else:
            print("Operação inválida, por favor selecione novamente.")

main()
