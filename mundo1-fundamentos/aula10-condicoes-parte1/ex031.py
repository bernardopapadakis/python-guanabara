"""
Exercício 031

Desafio: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
por Km para viagens de até 200Km e R$0,45 para viagens mais longas

Resolução:
"""
dis = float(input('Digite a distância da viagem em Km: '))
print('Você está prestes a iniciar uma viagem de {}Km'.format(dis))
if dis <= 200:
    valor = dis * 0.5
    print(f'Preço da passagem: R${valor}')
else:
    valor = dis * 0.45
    print('Preço da passagem: R${}'.format(valor))