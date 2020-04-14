"""
Exercício 048

Desafio:
    Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
encontram no intervalo de 1 atée 500

Resolução:
"""
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
print(f'A soma de todos os números ímpares múltiplos de 3 que vão de 1 a 500, resulta em {s}')