"""
Exercício 044

Desafio:
    Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros

Resolução:
"""
print('{:=^30}'.format(' LOJA '))
valor = float(input('Valor do produto: R$'))
print('''Método de pagamento:
[ 1 ] à vista dinheiro/cheque  
[ 2 ] à vista no cartão 
[ 3 ] em até 2x no cartão 
[ 4 ] 3x ou mais no cartão? ''')
method = input('Escolha uma opção: ')
if method == '1':
    print('Valor total a ser pago: R${:.2f}'.format(valor * 0.9))
elif method == '2':
    print('Valor total a ser pago: R${:.2f}'.format(valor * 0.95))
elif method == '3':
    p = valor / 2
    print('Você terá que pagar 2 parcelas de R${:.2f}'.format(p))
    print('Valor total a ser pago: R${:.2f}'.format(valor))
elif method == '4':
    pv = int(input('Quantas vezes você deseja parcelar? '))
    if pv == 3:
        p = valor / 3
        print('Você terá que pagar 3 parcelas de R${:.2f}'.format(p))
        print('Valor total a ser pago: R${:.2f}'.format(valor * 1.2))
    elif pv == 4:
        p = valor / 4
        print('Você terá que pagar 4 parcelas de R${:.2f}'.format(p))
        print('Valor total a ser pago: R${:.2f}'.format(valor * 1.2))
    elif pv == 5:
        p = valor / 5
        print('Você terá que pagar 5 parcelas de R${:.2f}'.format(p))
        print('Valor total a ser pago: R${:.2f}'.format(valor * 1.2))
    elif pv == 6:
        p = valor / 6
        print('Você terá que pagar 6 parcelas de R${:.2f}'.format(p))
        print('Valor total a ser pago: R${:.2f}'.format(valor * 1.2))
    else:
        print('Quantidade de parcelas inválida. Tente novamente')
else:
    print('Método de pagamento inválido. Tente novamente')