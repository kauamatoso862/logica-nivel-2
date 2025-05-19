# Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

nota1 = float(input("Digite a nota do 1º avaliação: "))
nota2 = float(input("Digite a nota do 2º avaliação: "))
media = (nota1 + nota2) / 2

print(f"A média é {media:.2f}")

if media >= 6: 
    print("Aprovado")
else:
    print("Reprovado")
