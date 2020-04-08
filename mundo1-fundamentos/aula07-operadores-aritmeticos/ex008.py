"""
Exercício 008

Desafio: Escreva um programa que leia um valor em metros e o exiba
convertido em centímetros e milímetros.

Resolução:
"""
n = float(input('Digite um número em metros para convertê-lo em centímetros e milímetros: '))
c = n*100
m = n*1000
print('O valor {}m em centímetros é igual a {:.0f}cm e em milímetros a {:.0f}mm'.format(n, c, m))
