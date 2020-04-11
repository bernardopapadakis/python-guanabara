"""
Exercício 043

Desafio:
    Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e moster seu status, de acordo com a
tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30 : Sobrepeso
- 30 até 40: Obesidade
- Acima de  40: Obesidade mórbida

Resolução:
"""
print('{:=^30}'.format(' CALCULO DE IMC '))
peso = float(input('Digite o seu peso: (kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / altura ** 2
if imc <= 18.5:
    print(f'IMC: {imc}, Você está ABAIXO DO PESO')
elif imc <= 25:
    print(f'IMC: {imc} Você está com o PESO IDEAL')
elif imc <= 30:
    print(f'IMC: {imc} Você está com SOBREPESO')
elif imc <= 40:
    print(f'IMC: {imc} Você está OBESIDADE')
else:
    print(f'IMC: {imc} Você está com OBESIDADE MÓRBIDA')