"""
Exercício 022:

Desafio: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras o nome tem no total (sem considerar espaços)
- Quantas letras tem o primeiro nome

Resolução:
"""
name = input('Digite seu nome completo: ').strip()
print('Seu nome em maiúsculas {}'.format(name.upper()))
print('Seu nome em minúsculas {}'.format(name.lower()))
print('Seu nome tem ao todo {} letras'.format(len(name)  - name.count(' ')))
lista = name.split()
print(('Seu primeiro nome é {} e ele tem {} letras'.format(lista[0], len(lista[0]))))