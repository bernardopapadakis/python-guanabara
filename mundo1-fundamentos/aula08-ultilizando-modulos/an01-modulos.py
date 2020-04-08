"""
    Módulos são funcionalidades que você pode importar para poder usá-las e para adicionarmos um módulo ou biblioteca
completa nós ultilizamos o comando import módulo.
"""
import math
import random

n = int(input('Digite um número: '))
raiz = math.sqrt(n)
print('A raiz qua drada de {} é igual a {:.2f}'.format(n, raiz))
n = random.randint(1, 99)
print('-' * 20)
print('Número aleatório usando o múdolo random: {}'.format(n))

