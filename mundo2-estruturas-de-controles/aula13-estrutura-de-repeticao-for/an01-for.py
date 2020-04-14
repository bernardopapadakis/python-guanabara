"""
    Laço de repetição com variável de controle FOR:
for <nome_do_laço_> in range(<começo_do_intervalo>, <final_do_intervalo>):
    <instrução>
"""
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    print(c)
for oi in range(0, 6, 2 ):
    print('Hello World!')
for io in range(n, 0, -1):
    print(io)
print('FIM')
for separador in range(0,3):
    print('='*60)
i = int(input('Início: '))
f = int(input('Fim: '))
for co in range(i, f):
    print(co)
