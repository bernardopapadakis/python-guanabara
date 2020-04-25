"""
Exercício 021

Desafio: Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.

Resolução:
"""
from playsound import playsound

n1 = int(input('[ 1 ] Escutar música\n[ 2 ] Sair\nSua resposta: '))
if n1 == 1:
    print('Processando')
    playsound('C:/programming/estudo/python/python-cursoemvideo/mundo1-fundamentos/aula08-ultilizando-modulos/ex021.mp3')
else:
    print('Tchau!!')
