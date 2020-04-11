"""
    Condicionais Aninhadas:

if condição1:
    instrução1
elif condição2:
    instrução2 
else:
    instrução3
"""
nome = str(input('Digite seu nome: ')).strip()
if nome == 'Bernardo':
    print('Que nome lindo!')
elif nome == 'Guanabara':
    print('Que nome de professor!')
elif nome == 'Pedro' or nome == 'João' or nome =='Maria ':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é bem comum')
print('Tenha um bom dia')