"""
    Existe outra forma de juntar dois valores dentro de um print sem ser usando o + ou ,
,essa forma é o método .format().
"""
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
s = n1 + n2
print('A soma vale',s)# sem .format
print('A soma vale {}'. format(s))# com .format