# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

brancos = int(input("Qual a quantidade de votos brancos? "))
nulos = int(input("Qual a quantidade de votos nulos? "))
validos = int(input("Qual a quantidade de votos válidos? "))


total = brancos + nulos + validos


percentual_brancos = (brancos / total) * 100
percentual_nulos = (nulos / total) * 100
percentual_validos = (validos / total) * 100


print(f"Total de votos válidos: {percentual_validos:.2f}%")
print(f"Total de votos em branco: {percentual_brancos:.2f}%")
print(f"Total de votos nulos: {percentual_nulos:.2f}%")
