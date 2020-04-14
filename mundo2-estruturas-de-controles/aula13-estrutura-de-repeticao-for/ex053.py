"""
Exercício 053

Desafio:
    Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Resolução:
"""
frase = input("Digite uma frase: ").upper().replace(" ", "")
j = frase[::-1]
print(f'{frase} ao contrário é {j}')
if frase == j:
    print("Portanto a frase É um palíndromo")
else:
    print("Portanto a frase NÃO É um palíndromo")