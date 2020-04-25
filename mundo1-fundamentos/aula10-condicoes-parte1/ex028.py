"""
Exercício 028

Desafio:
    Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo o computador.
    O programa deverá escrever na tela se o usuário venceu ou perdeu.

Resolução:
"""
from playsound import playsound
from random import randint
from time import sleep
n = randint(0, 5)# Escolhe um número aleatório entre 0 e 5
print('\033[1;34m--'*40)
print('{:^86}'.format('\033[1;30mVou pensar em um número entre 0 e 5. Tente adivinhar!'))
print('\033[1;34m--'*40)
r = int(input('\033[1;30mEm que número eu pensei? '))# Jogador tenta adivinhar o número
print('\033[1;33mPROCESSANDO...')
sleep(1)
if r == n:
    print(f'\033[1;32mParabéns, você acertou!')
    playsound('C:/pg/estudo/curso-em-video/python/mundo1-fundamentos/aula10-condicoes-parte1/ex028-win.mp3')
else:
    print(f'\033[1;31mVocê errou! Eu tinha pensando em {n}. Tente novamente!')
    playsound('C:/pg/estudo/curso-em-video/python/mundo1-fundamentos/aula10-condicoes-parte1/ex028-loss.wav')