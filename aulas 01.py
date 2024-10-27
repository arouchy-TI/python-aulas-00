#def sacar(valor):
    
#    saldo = 10000

#    if saldo >= valor:
#        print("valor sacado com sucesso")


#def depositar(valor):
#    Saldo = 10000
#    Saldo += valor    
#    print(f"Deposito Realizado,Saldo:{Saldo}")

#sacar(1000)
#depositar(200)

# ESTRUTURAS CONDICIONAIS 

#opcao = int(input("Digite [1] para sacar /n Digite [2] para ver o extrato "))

#if opcao == 1:
#    valor = float(input("Digite o valor para saque: "))

#elif opcao == 2:
#    print("Exibindo o valor do extrato... ")

#else:
#    print("Opção Inválida")
    


#Maior_idade = 18
#Idade_Especial = 12

#idade = int(input("Informe a sua idade: "))

#if idade >= Maior_idade:
#    print("Maior de idade pode tirar a CNH")

#elif idade == Idade_Especial:
#    print("Pode realizar aulas praticas")

#else:
#    print("Menor de idade,não pode tirar CNH")


# ELSE/IF ANINHADO

#Conta_Normal = False
#Conta_Universitaria = False
#Conta_Especial = True

#saldo = 2000
#saque = 2600
#Cheque_Especial = 500

#if Conta_Normal:
#    if saldo >= saque:
#        print("Saque realizado com sucesso")
#    elif saque <= (saldo + Cheque_Especial):
#        print("Saque realizado com cheque especial")
#    else:
#        print("Nao foi possível realizar saque.Saldo insuficiente ")


#elif Conta_Universitaria:
#    if saldo >= saque:
#        print("Saque realizado com sucesso")
#    else:
#        print("Saldo insuficiente ")

#elif Conta_Especial:
#    print("Conta especial selecionada")

#else: 
#    print("Conta não identificada,entre em contato com o gerente ")


# IF TERNÁRIO

#Saldo = 1000
#Saque = 500

#Status = "Sucesso" if Saldo >= Saque else "falha"

#print(f"{Status} ao realziar operação Saque!")


# ESTRUTURAS DE REPETIÇÃO

#Texto = input("informe um texto ")
#VOGAIS = "AEIOU"

#for letras in Texto:
#    if letras.upper() in VOGAIS:
#        print(letras, end="")
#print()


# list(range(10))

#for lista in range(0,10):
#    print(lista, end=" ")

# range (start,stop[,step]) -> range object

#for lista01 in range(0,51,5):
#    print(lista01)

#opcao = -1

#while opcao != 0:
#    opcao = int(input("[0] Sacar \n [1] Extrato \n [2] Sair \n"))

#    if opcao == 0:
        
#        print(f"Sacando...")

    
#    elif opcao == 1:
#        print("Emitindo extrato...")

#    elif opcao == 2:
#        print("Saindo...")

#else:
#    print("Obrigado por usar nosso sistema ")


#while True:
#    numero = int(input("Digite um numero "))
#    if numero == 10:
#       print("achou..")
#        break
        

#print(numero)

#for numero in range(100):
#    if numero == 12:
#        continue
#    if numero == 20:
#        continue
#    print(numero, end=" ")

# while True:
#    numero = int(input("Digite um numero "))

#    if numero == 10:
#        break

#    if numero % 2 == 0:
#        continue