"""
Exercício 029

Desafio:
    Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$7,00 por cada Km acima do limite.

Resolução
"""

velocidade = float(input('Qual a velocidade atual do seu carro? '))
if velocidade >= 80:
    m = (velocidade - 80) * 7
    print('\033[1;31mMULTADO! Você exedeu o limite de 80Km/h \n'
          '\033[1;31mR$Valor da multa: \033[1;33m${:.2f}'.format(m))
print('\033[32mTenha um bom dia! Dirija com segurança!')
