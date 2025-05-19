#  O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor. 

custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))

distribuidor = custo_fabrica * 0.28
impostos = custo_fabrica * 0.45

custo_final = custo_fabrica + distribuidor + impostos

print(f"Custo final ao consumidor: R$ {custo_final:.2f}")
