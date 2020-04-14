"""
Exercício 056

Desafio:
    Desenvolva um prograama que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
    
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos

Resolução:
"""
totidade = 0
médiaidade = 0
idademaisvelho = 0
totmulher20 = 0
homemmaisvelho = ''

for c in range(1, 5):
    print(f'---- {c}ª pessoa ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    totidade += idade
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
    if c == 1 and sexo in 'Mm':
        homemmaisvelho = nome
        idademaisvelho = idade
    if sexo in 'Mm' and idade > idademaisvelho:
        idademaisvelho = idade
        homemmaisvelho = nome

médiaidade = totidade / 4
print(f'A idade média do grupo é {médiaidade} anos')
print(f'O homem mais velho tem {idademaisvelho} e se chama {homemmaisvelho}')
print(f'{totmulher20} mulheres tem menos de 20 anos')