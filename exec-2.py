#Os pares de instruções abaixo produzem o mesmo resultado? Imprima os valores abaixo, veja se algum deles (A, B ou C) possuem valores diferentes nas versões 1 e 2, e caso sim, explique num comentário o motivo.

A1 = (4/2) + (2/4)
A2 = 4/2 + 2/4

B1 = 4/(2+2)/4
B2 = 4/2 + 2/4

C1 = (4+2) *2-4
C2 = 4+2*2-4

print(f"A1 = {A1}, A2 = {A2}")
print(f"B1 = {B1}, B2 = {B2}")
print(f"'C1 = {C1}, C2 = {C2}")

#Razao
#A1 e A2 são iguais, pois a ordem das operações não mudam o resultado.
#B1 e B2 não são iguais, porque os parênteses altera a ordem das divisões.
#C1 e C2 não são iguais, porque a multiplicação vem primeiro que a adição.