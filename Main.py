'''
Caso de Uso

Criar uma conta bancaria com deposito, saque e extrato

deposito: 

- deve ser possivel depositar valores positivos

Saque:

- o sistema deve permitir 3 saques por dia
- maximo 500 reais por saque
- se nao houver saldo para o saque, informar e cancelar operação

Extrato:

- mostrar todas as operações de saque e deposito da conta

'''
import os

depositar = 0
saldo = 0
sacar = 0
cont = 0
extrato = []


print("Bem vindo ao Banco Kalil's data")

opcao = input("Qual operação deseja realizar? \n[1] Sacar \n[2] Depositar \n[3] Extrato \n[4] Sair \n \n")

while opcao != "4":

    if opcao == "1":
        sacar = input("Digite o valor que deseja sacar: ")

        if sacar.isdigit():
            sacar = int(sacar)

            if cont >= 3:
                print("Limite maximo de saques diarios atingidos")
                opcao = input("Qual operação deseja realizar? \n[1] Sacar \n[2] Depositar \n[3] Extrato \n[4] Sair \n \n")

            elif cont < 3:

                if sacar <= 500:

                    if sacar <= saldo:

                        saldo -= sacar
                        extrato.append(f"-{sacar}")
                        cont += 1
                        os.system('cls')
                        print(f"Saldo atual: {saldo}")

                        opcao = input("Qual operação deseja realizar? \n[1] Sacar \n[2] Depositar \n[3] Extrato \n[4] Sair \n \n")
    
                    elif sacar > saldo:
                        print("Saldo insuficiente")

                        opcao = input("Qual operação deseja realizar? \n[1] Sacar \n[2] Depositar \n[3] Extrato \n[4] Sair \n \n")

                elif sacar > 500:
                    print("Valor maximo para saque ultrapassado, limite: R$ 500")
                    opcao = input("Qual operação deseja realizar? \n[1] Sacar \n[2] Depositar \n[3] Extrato \n[4] Sair \n \n")

    elif opcao == "2":
        
        depositar = input("Qual valor deseja depositar? ")

        if depositar.isdigit():
            depositar = int(depositar)

            if depositar > 0:

                extrato.append(f"+{depositar}")
                saldo += depositar
                os.system('cls')
                print(f"Saldo atual: {saldo}")
 
                opcao = input("Qual operação deseja realizar? \n[1] Sacar \n[2] Depositar \n[3] Extrato \n[4] Sair \n \n")

            else:
                print("valor negativo nao permitido")

        else:
            print("Voce nao digitou um valor valido")

    elif opcao == "3":
        
        os.system('cls')
        print("Exibindo seu Extrato")

        for i in extrato:
            print(f"R$ {i}")
        print(f"Saldo da conta: {saldo}")

        opcao = input("Qual operação deseja realizar? \n[1] Sacar \n[2] Depositar \n[3] Extrato \n[4] Sair \n \n")

    else:
        print("Opção invalida")

        opcao = input("Qual operação deseja realizar? \n[1] Sacar \n[2] Depositar \n[3] Extrato \n[4] Sair \n \n")

os.system("cls")     
print("Fazendo logout... \n \nObrigado por utilizar o Banco Kalil's data")
print("""
         _____
       /       \\
      |  O   O  |
      |    ^    |
      |  \\___/  |
       \\_______/
""")



# I W B B


