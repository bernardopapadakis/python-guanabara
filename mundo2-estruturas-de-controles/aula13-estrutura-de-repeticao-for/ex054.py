"""
Exercicio 054

Desafio:
    Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores.

Resolução:
"""
from datetime import date
aa = date.today().year
m21 = 0
for c in range(1, 8):
    p = int(input(f'Em que ano nasceu a {c}ª pessoa? '))
    if aa - p >= 21:
        m21 += 1
print(f'Ao todo {m21} são maiores de idade')
print(f'Ao todo {7 - m21} são menores de idade')