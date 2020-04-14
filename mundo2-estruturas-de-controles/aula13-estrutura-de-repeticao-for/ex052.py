"""
Exercício 052

Desafio:
    Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

Resolução:
"""
n = int(input('Digite um número: '))
t = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')

if t == 2:
    print((f'\033[m\nO número {n} é pode ser dividido {t} vezes\nPortanto é um número PRIMO!'))
else:
    print(f'\033[m\nO número {n} é pode ser dividido {t} vezes\nPortanto ele NÃO É PRIMO!')