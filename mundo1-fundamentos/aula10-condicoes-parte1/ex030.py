"""
Exercício 30

Desafio: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

Resolução:
"""
num = int(input('\033[35mDigite um número para saber se ele é par ou ímpar: \033[m'))
r = num % 2
if r == 0:
    print(f'{num} é \033[34mPAR!')
else:
    print(f'{num} é \033[34mIMPAR!')