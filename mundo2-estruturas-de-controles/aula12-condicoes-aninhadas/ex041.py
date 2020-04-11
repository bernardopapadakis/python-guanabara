"""
Exercício 041

Desafio:
    A Confederação Nacional de Natação prescisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER

Resolução:
"""
idade = int(input('Digite a sua idade: '))
if idade <= 9:
    print('você é considerado MIRIM')
elif idade <= 14:
    print('você é considerado INFANTIL')
elif idade <= 19:
    print('você é considerado JUNIOR')
elif idade <=25:
    print('você é considerado SÊNIOR')
else:
    print('você é considerado MASTER')
