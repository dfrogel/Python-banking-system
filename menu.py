menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

def print_erro_mensagem(mensagem):
    print("Erro de operação. " + mensagem)

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor que você deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print_erro_mensagem("O valor informado é inválido!")

    elif opcao == "2":
        valor = float(input("Informe o valor que você deseja sacar: "))
        if valor > 0:
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saque = numero_saque >= LIMITE_SAQUE

            if excedeu_saldo:
                print_erro_mensagem("Você não tem saldo suficiente para realizar o saque!")
            elif excedeu_limite:
                print_erro_mensagem("O valor do saque excede o limite disponível!")
            elif excedeu_saque:
                print_erro_mensagem("Você excedeu seu limite diário!")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saque += 1
        else:
            print_erro_mensagem("O valor informado é inválido!")

    elif opcao == "3":
        print("\n##########EXTRATO##########")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"\nSaldo: {saldo:.2f}")
        print("###########################")

    elif opcao == "4":
        print("Saindo...")
        break

    elif opcao == "0":
        pass  # Nenhuma operação, apenas exibir o menu novamente.

    else:
        print("Por favor, insira uma opção válida!")
