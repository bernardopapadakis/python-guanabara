"""
Exercício 034

Desafio:
    Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
    Para salários superiores a R$1.250,00, calcule um aumento de 10%.
    Para os inferiores ou iguais o aumento é de 15%

Resolução:
"""
salario = float(input('Digite o salário do funcionário: R$'))
if salario <= 1250:
    print('O funcionário agora passa a ganhar {}'.format(salario + salario * 0.15))
else:
    print('O funcionário agora passa a ganhar {}'.format(salario + salario * 0.1))