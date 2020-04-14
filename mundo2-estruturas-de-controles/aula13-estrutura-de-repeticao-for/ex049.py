"""
Exercício 049

Desafio:
    Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora ultilizando um
laço for.

Resolução:
"""
print('{:=^40}'.format(' TABUADA '))
n = int(input('Digite um número inteiro para saber sua tabuada até 10: '))
for c in range(1, 11):
    print(f'{n} x {c} = {n * c}')
