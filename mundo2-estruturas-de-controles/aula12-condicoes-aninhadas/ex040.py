"""
Exercício 040

Desafio:
    Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÂO
- Média 7.0 ou superior: APROVADO

Resolução:
"""
print('{:=^30}'.format(' MÈDIA '))
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('Aluno REPROVADO\nMédia: {:.2f}'.format(m))
elif m < 7.0:
    print('Aluno RECUPERAÇÃO\nMédia: {:.2f}'.format(m))
else:
    print('Aluno APROVADO\nMédia: {:.2f}'.format(m))

