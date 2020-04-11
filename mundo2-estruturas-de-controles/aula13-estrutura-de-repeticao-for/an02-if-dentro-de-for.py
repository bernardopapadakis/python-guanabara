"""
Condicionais dentro de laços de repetições:
for <nome_do_laço_> in range(<começo_do_intervalo>, <final_do_intervalo>):
    if <condição>:
        <instrução_if>
    <instrução_for>
"""

for c in range(0, 10):
    n = float(input('Digite um número: '))
    if n < 10:
        print('Seu número tem UNIDADE !')
    elif n < 100:
        print('Seu número tem UNIDADE e DEZENA!')
    elif n < 1000:
        print('Seu número tem UNIDADE, DEZENA e CENTENA!')
    else:
        print('Seu número é ENORME!')
print('Tenha um bom dia!')