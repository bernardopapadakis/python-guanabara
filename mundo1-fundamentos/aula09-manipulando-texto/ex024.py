"""
Exercício 024

Desafio: Crie um prorgama que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

Resolução
"""
c = str(input('Digite a cidade que você nascecu: ')).strip().upper()
print(c[:5] == 'SANTO')