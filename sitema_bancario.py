menu = """

###### MENU ######

[d] Depositar
[s] Sacar
[e] Extrato
[q] sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

while True:

    
    opcao = input(menu)


    if opcao == 'd':
        valor = float(input("informe o valor do deposito: "))

        if valor <= 0:
            print("impossivel a realizar esse saque")
        
        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

            
    elif opcao == 's':
       

        
            valor = float(input("informe o valor do saque (limite de saque = R$500) "))
            
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saque = numero_saque > limite_saque

            if excedeu_saldo:
                print("Erro! nao existe saldo suficiente")
            elif excedeu_limite:
                print("Seu saque passou do limite pre estabelicido")
            elif excedeu_saque:
                print("Tentativa de saque diario excedida, volte amanha")
           
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saque += 1
            else:
                print("Falha! OPERACAO INVALIDA")

                

    elif opcao == 'e':

        print("====================extrato======================/n")
        print("Nao existe movimnetacao /n" if not extrato else extrato)
        print(f"Seu Saldo atual = {saldo:.2f}/n")
        print("==================================================")

        
    elif opcao == 'q':
        break
    else:
        print("Selecione algo valido")
            
        

           
           
           
        

           
           
           
           
            

        
            

        



            


        



