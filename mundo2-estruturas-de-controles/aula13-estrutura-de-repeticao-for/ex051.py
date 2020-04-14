"""
Exercício 051

Desafio:
    Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primmeiros
termos dessa progressão.

Resolução:
"""
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(pt, pt + r * 10, r):
    print(c)