"""
Exercício 039

Desfaio:
    Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar
- Se já passou do tempo do alistamento.

    Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

Resolução:
"""
from datetime import date

print('{:=^30}'.format(' ALISTAMENTO '))
an = int(input('Digite o seu ano de nascimento: '))
s = input('Você é homem ou mulher? ')
aa = date.today().year
idade = (aa - an)
if s == 'homem':
    if idade < 18:
        a = 18 - idade
        print(f'Você ainda vai se alistar no serviço militar em {a + aa}\nFaltam apenas {a} anos, prepare-se!')
    elif idade == 18:
        print('Está no ano de se alistar para o serviço militar!\nAliste-se IMEDIATAMENTE!')
    else:
        a = idade - 18
        print(f'Seu ano de alistamento foi em {an + 18}\nJá se passaram {a} anos')
else:
    print('Você não prescisa servir o exército.')
