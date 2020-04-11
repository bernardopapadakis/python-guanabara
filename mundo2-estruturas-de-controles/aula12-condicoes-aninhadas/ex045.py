"""
Exercício 045

Desafio:
    Crie um programa que faça o compputador jogar Jokenpô com você.

Resolução:
"""
from random import choice
from time import sleep

print('{:=^30}'.format(' JOKENPÔ '))
print('''[ 1 ] pedra 
[ 2 ] papel 
[ 3 ] tesoura? ''')
j = int(input('Faça sua escolha: '))
c = choice(['pedra', 'papel', 'tesoura'])
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)
if j == 1 and c == 'tesoura' or j == 2 and c == 'pedra' or j == 3 and c == 'papel':
    print(f'VITÓRIA!!')
elif j == 1 and c == 'pedra' or j == 2 and c == 'papel' or j == 3 and c == 'tesoura':
    print(f'EMPATE')
elif j == 1 and c == 'papel' or j == 2 and c == 'tesoura' or j == 3 and c == 'pedra':
    print(f'DERROTA!')
else:
    print('Dado inválido. Tente novamente')