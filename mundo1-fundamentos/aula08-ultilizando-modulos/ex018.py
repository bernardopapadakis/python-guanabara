"""
Exercício 018

Desafio: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangengente desse ângulo.

Resolução:
"""
from math import sin, cos, tan, radians

a = float(input('Digite ângulo: '))
se = sin(radians(a))
co = cos(radians(a))
t = tan(radians(a))
print('Seno: {:.2f}\n'
      'Cosseno: {:.2f}\n'
      'Tangente: {:.2f}'.format(se, co, t))