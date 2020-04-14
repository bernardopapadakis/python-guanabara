"""
Exercício 050:

Desafio:
    Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se
o valor digitado for ímpar, desconsidere-o.


Resolução:
"""
soma = 0
count = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        count = count + 1
        soma += n
if count == 1:
    print(f'Você digitou {count} número par, que vale {soma}')
else:
    print(f'Você digitou {count} números pares e a soma entre eles resulta em {soma}')