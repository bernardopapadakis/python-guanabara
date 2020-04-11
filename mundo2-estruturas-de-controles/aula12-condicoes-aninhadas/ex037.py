"""
Exercício 037

Desafio:
    Escreva um programa que leia um número inteiro qualquer e peça pera o usuário escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal

Resolução:
"""
print('{:=^30}'.format(' CONVERSOR DE BASES '))
n = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções para fazer a conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input('Digite a sua opção: '))
if op == 1:
    print('{} convertido para BINÁRIO é {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(n, hex(n)[2:]))
else:
    print('Opção Inválida. Tente novamente.')
