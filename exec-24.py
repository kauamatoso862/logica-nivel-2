# Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

numero_conta = input("Digite o número da conta: ")
saldo = float(input("Digite o saldo da conta: "))
debito = float(input("Digite o valor do débito: "))
credito = float(input("Digite o valor do crédito: "))


saldo_atual = saldo - debito + credito


print(f"\nConta Nº: {numero_conta}")
print(f"Saldo atual: R$ {saldo_atual:.2f}")


if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")
