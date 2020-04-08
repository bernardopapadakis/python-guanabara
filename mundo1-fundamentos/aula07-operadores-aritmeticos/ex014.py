"""
Exercício 014

Desafio: Escreva um progama que converta uma temperatura digitada em °C e converta para °F.

Resolução:
"""
c = float(input('Digite a temperatura em °C: '))
f = c * 9 / 5 + 32
print('{}°C é igual a {}°F'.format(c, f))