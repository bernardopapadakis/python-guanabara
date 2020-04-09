"""
Exercício 032

Desafio: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

Resolução:
"""
from datetime import date
ano = int(input('Digite um ano para saber se ele é BISSEXTO (ano 0 conta como ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano BISSEXTO!')
else:
    print(f'{ano} não é um ano BISSEXTO')