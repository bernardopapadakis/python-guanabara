"""
Exercício 015

Desafio: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
carro custa R$60 por dia e R$0,15 por km rodado.

Resolução:
"""
km = float(input('Quantos km você rodou com o carro alugado? '))
dias = int(input('Por quantos dias você alugou ele? '))
p = (60 * dias) + (0.15 * km)
print('Preço a pagar: R${:.2f}'.format(p))