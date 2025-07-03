menu =  """

[d] Depositar
[s] Sacar   
[e] Extrato 
[q] Sair 

=>"""

saldo = 0
limite = 500
extrato = ""    
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opacao = input(menu)

    if opacao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido. O depósito deve ser positivo.")
    elif opacao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Informe o valor do saque: "))
            if 0 < valor <= saldo:
                saldo -= valor
                if valor > limite:
                    print(f"Valor do saque excede o limite de R$ {limite:.2f}.")
                    continue    
                extrato += f"Saque: R$ {valor:.2f}\
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Valor inválido. O saque deve ser positivo e não pode ultrapassar o saldo.")
        else:
            print("Limite de saques atingido.")
    elif opacao == "e":
        if extrato:
            
            print("=== Extrato ===")
            print(extrato)
            print(f"Saldo: R$ {saldo:.2f}")
        else:
            print("Nenhum movimento encontrado.")
    elif opacao == "q":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")           
