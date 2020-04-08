"""
Exercício 011

Desafio: Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a
sua área e a quantidade de tinta necessária para pintá-la. Sabendo que cada litro de tinta
pinta uma área de 2 metros quadrados.

Resolução
"""
larg =float(input('Largura da parede em metros: '))
alt = float(input('Altura da parede em metros: '))
a = larg * alt
print('A sua parede tem uma área de {}, portanto você vai prescisar de {} litros de tinta para pintá-la'.format(a, a/2))