"""
    Laço de repetição com teste lógico WHILE:
while not <teste_lógico>:
    <instrução>
"""
'''for c in range(0,10):
    print(c)
print('FIM')'''
# ==
c = 0
while c <= 10:
    print(c)
    c += 1
print('FIM')
print('{:=^40}'.format(' WHILE INFINITO '))
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N]')).upper()
print('"infinito" kk')
