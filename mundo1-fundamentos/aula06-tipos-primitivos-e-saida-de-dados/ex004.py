"""
Exercício 004

Desafio: Faça um progama que leia algo pelo teclado e mostre na tela o seu tipo
primitivo e todas as informações possíveis sobre ele.

Resolução:
"""
algo = input('Digite algo: ')
print('O tipo primitivo de {} é'.format(algo), type(algo))
print('Só tem espaços?', algo.isspace())
print('É um número?', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('Está em maiúsculas?', algo.isupper())
print('Está em minúsculas?', algo.islower())
print('Está capitalizada?', algo.istitle())