"""
Exercício 027

Desafio: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

Resolução:
"""
name = str(input('Digite o seu nome completo: ')).strip()
lista = name.split()
print('Seu primeiro nome é {}'.format(lista[0]))
print('Seu última nome é {}'.format(lista[(len(lista) - 1)]))
