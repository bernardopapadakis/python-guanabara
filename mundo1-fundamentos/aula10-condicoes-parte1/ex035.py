"""
Exercício 035

Desafio: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

Resolução:
"""
print('_'*50)
print('Validador de triângulos!')
print('_'*50)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro  segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos digitados PODEM formar um triângulo')
else:
    print('Os segmentos digitados NÂO PODEM formar um triângulo')
