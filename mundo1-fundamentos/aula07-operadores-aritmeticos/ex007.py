"""
Exercício 007

Desafio: Desenvolva um progama que leia as duas notas de um aluno. Calcule
e mostre a sua média.
"""
print('Pronto para calcular sua média?')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
m = (nota1+nota2)/2
print('A sua média é {:.1f}'.format(m))