print("Olá! Qual é o seu nome?")
nome = input()

print("Digite seu saldo atual.")
saldo = float(input())

print("Bem-vindo(a),", nome,", o que deseja fazer hoje?\na. Sacar dinheiro\nb. Depositar dinheiro")
opção = input()

if opção == "b":
    print("Quanto deseja depositar?")

else:
    print("Digite uma opção válida, por favor.")

depósito = float(input())

print("Certo! Seu saldo atual é de", saldo+depósito,". Volte Sempre!")
