# Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.

inicio = int(input("Digite a hora de início do jogo (0-23): "))
fim = int(input("Digite a hora de fim do jogo (0-23): "))

if inicio < fim:
    duracao = fim - inicio
else:
    duracao = (24 - inicio) + fim

print(f"A duração do jogo foi de {duracao} hora(s).")
