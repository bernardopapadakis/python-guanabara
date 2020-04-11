"""
Exercício 042

Desafio:
    Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno : Todos laods diferentes

Resolução:
"""
print('{:=^40}'.format('VALIDADOR DE TRIÂNGULOS'))
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro  segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos digitados PODEM formar um triângulo', end=' ')
    if r1 == r2 == r3:
         print('EQUILÁTERO')
    elif r1 != r2 != r3:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos digitados NÂO PODEM formar um triângulo')