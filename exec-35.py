#Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90. 

litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A - Álcool, G - Gasolina): ").upper()


preco_alcool = 2.90
preco_gasolina = 3.30


if tipo == 'A':
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    preco_bruto = litros * preco_alcool
    valor_desconto = preco_bruto * desconto
    valor_total = preco_bruto - valor_desconto

elif tipo == 'G':
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    preco_bruto = litros * preco_gasolina
    valor_desconto = preco_bruto * desconto
    valor_total = preco_bruto - valor_desconto

else:
    print("Tipo de combustível inválido.")
    valor_total = None

if valor_total is not None:
    print(f"Valor a ser pago: R$ {valor_total:.2f}")
