"""
Exercício 016

Desafio: Crie um progama que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

Resolução:
"""
from math import trunc

n = float(input('Digite um número real: '))
print('O número {} tem o valor inteiro {}'.format(n, trunc(n)))# ou int(n)