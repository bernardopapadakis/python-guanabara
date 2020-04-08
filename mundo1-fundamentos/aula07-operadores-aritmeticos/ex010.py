"""
Exercício 010

Desafio: Crie um progama que leia quanto dinheiro uma pessoa tem na carteira e mostre
quantos dólares ela pode comprar.

Resolução:
"""
reais = float(input('Digite quantos reais você tem, para saber quantos dólares você pode comprar. R$'))
print('Voce pode adquirir {:.2f} dólares com {:.2f} reais'.format(reais/5.25, reais))