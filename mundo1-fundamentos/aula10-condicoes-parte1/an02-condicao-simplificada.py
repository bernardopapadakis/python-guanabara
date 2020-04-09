"""
    Condicionais simples:

instruçãoV if condição else instruçãoF
"""
tempo = int(input('Quantos anos tem o seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')
print('-'*10, 'FIM', '-'*10)