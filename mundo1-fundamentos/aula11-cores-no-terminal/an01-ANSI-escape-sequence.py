"""
    Para colocar cores em textos, nós usamos o padrão ANSI escape sequence: \033[style;text;back
- style: estilo da fonte, negrito, sublinhado...
- text: cor do texto, amarelo, zazul...
- back: cor do background, preto, branco...
    STYLE:
- 0: none
- 1: bold
- 4: underline
- 7: negative
    TEXT:
- 30: branco
- 31: vermelho
- 32: verde
- 33: amarelo
- 34: azul
- 35: roxo
- 36: azul claro
- 37: cinza
    BACK
- 40: branco
- 41: vermelho
- 42: verde
- 43: amarelo
- 44: azul
- 45: roxo
- 46: azul claro
- 47: cinza

    Para voltar a cor padrão: \033[m
"""
print('-=-' * 35)
print('EXEMPLOS PRÁTICOS:')
print('-=-' * 35)
print('\033[1;34;40mTexto em negrito, com o texto em azul e o background branco\033[m')
print('\033[4;35mTexto sublinhado, com o texto em roxo e o background padrão\033[m')
print('\033[7;33mTexto em negative, com o texto em amarelo e o background padrão\033[m')
print('\033[31mTexto padrão, com o texto em vermelho e o background padrão\033[m')
# Outra forma é criar um variável e guardar o código de cada cor nela
print('-=-' * 35)
print('USANDO VARIÁVEIS:')
print('-=-' * 35)
name = input('Digite sue nome: ')
cores = {'limpa': '\033[m',
         'azul': '\033[33m',
         'amarelo': '\033[33m',
         'petroebranco': '\033[7:30m'}
print('Prazer em te conhecer {}{}{}!'.format(cores['petroebranco'], name, cores['limpa']))
