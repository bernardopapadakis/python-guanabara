"""
    Nós podemos importar bibliotecas que não são instaladas por padrão, importando elas normalmente, clicando em cima
do código do módulo, clicando na lâmpada vermelha e instalando, ou rodar no terminal o código para instalar o módulo,
como exemplo: pip install emoji --upgrade
"""
import emoji
print(emoji.emojize('Pyton é perfeito! :smile:', use_aliases=True))