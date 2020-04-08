"""
Exercício 006

Desafio: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

Resolução:
"""
n = float(input('Digite um número para saber o seu dobro, seu triplo e sua raiz quadrada: '))
print('Dobro: {}\nTriplo: {}\nRaiz quadrada: {:.2f}'.format((n*2), (n*3), (n**(1/2))))