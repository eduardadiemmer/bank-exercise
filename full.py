print("Olá! Qual é o seu nome?")
nome = input()

print("Digite seu saldo atual.")
saldo = float(input())

print("Bem-vindo(a),", nome,", o que deseja fazer hoje?\na. Sacar dinheiro\nb. Depositar dinheiro")
opção = input()

if opção == "a":
    print("Quanto deseja sacar?")
    valor_a_mexer = float(input()) * -1

elif opção == "b":
    print("Quanto deseja depositar?")
    valor_a_mexer = float(input())

saldo = saldo + valor_a_mexer

if saldo < 0:
    print("Saldo insuficiente.")

else:
    print("Certo! Seu saldo atual é de", saldo,". Volte Sempre!" )