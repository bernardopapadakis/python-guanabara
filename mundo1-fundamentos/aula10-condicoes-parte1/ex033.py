"""
Exercício 033

Desafio: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

Resolução:
"""
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
menor = n1
# Verificando o menor número
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1  and n3 < n2:
    menor = n3
print(f'{menor} é o menor número')
# Veridicando o maior número
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1  and n3 > n2:
    maior = n3
print(f'{maior} é o maior número')

