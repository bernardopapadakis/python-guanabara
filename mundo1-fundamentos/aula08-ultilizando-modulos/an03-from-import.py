"""
    Para adicionarmos uma funcionalidade específica de um módulo, você usa from módulo import
funcionalidade específica.
"""
from math import sqrt
n = int(input('Digite um número: '))
raiz = sqrt(n)
print('A raiz qua drada de {} é igual a {:.2f}'.format(n, raiz))
