print("Olá! Qual é o seu nome?")
nome = input()

print("Digite seu saldo atual.")
saldo = float(input())

print("Bem-vindo(a),", nome,", o que deseja fazer hoje?\na. Sacar dinheiro\nb. Depositar dinheiro")
opção = input()

if opção == "a":
    print("Quanto deseja sacar?")

else:
    print("Digite uma opção válida, por favor.")

saque = float(input())

if saque > saldo:
    print("Saldo insuficiente.")

elif saque <= saldo:
    print("Certo! Seu saldo atual é de", saldo-saque,". Volte Sempre!" )
