"""
Exercício 017

Desafio: Faça um progama que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
e mostre o comprimento da hipotenusa.

Resolução:
"""
from math import hypot

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
# h = (co**2 + ca**2)**0.5
# print('Hipotenusa: {:.2f}'.format(h))
# ou
h = hypot(co, ca)
print('Hipotenusa: {:.2f}'.format(h))
