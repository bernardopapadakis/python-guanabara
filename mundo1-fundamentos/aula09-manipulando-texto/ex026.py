"""
Exercício 026

Desafio: Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A"
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.

Resolução:
"""
algo = str(input(('Digite uma frase: '))).strip().lower()
print('A letra A aparece {} vezes na frase'.format(algo.count('a')))
print('A primeira letra A apareceu na posição {}'.format(algo.find('a') + 1))
print('A última letra a apareceu na poscição {}'.format(algo.rfind('a') + 1))