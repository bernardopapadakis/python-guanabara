"""
Exercício 036

Desafio:
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.

    Calcule o valor da prestação mensal. Sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

Resolução:
"""
# Título do exercício
print('{:=^40}'.format('\033[1m EMPRÉSTIMO \033[m'))
# Entrada de dados
casa = float(input('Digite o valor da casa que você deseja comprar: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Em quantos anos você pretende pagar o empréstimo? '))
# Processamento de dados & saída de dados
pm = casa / (anos * 12)
if (salario * 0.3) >= pm:
    print('EMPRÉSTIMO ACEITO!\nValor da casa {:.2f}\nvalor a ser pago todo mês: R${:.2f}\nDuração: {}'.format(casa, pm, anos))
else:
    print('EMPRÉSTIMO NEGADO!')
print('Tenha um bom dia!')

