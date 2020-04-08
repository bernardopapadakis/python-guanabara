"""
Exercício 025

Desafio: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA' no nome.

Resolução:
"""
name = input('Digite seu nome completo: ').strip()
print('Seu nome tem Silva? {}'.format('silva' in name.lower()))