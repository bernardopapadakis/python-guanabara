"""
Exercício 013

Desafio: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário
com 15% de aumento.

Resolução:
"""
salário = float(input('Digite o salário do funcionário: '))
print('O mesmo funcionário receberia R${} se recebesse 15% de aumento'.format(salário * 1.15))