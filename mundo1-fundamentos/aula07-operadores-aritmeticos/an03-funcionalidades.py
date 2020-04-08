print('-'*20)
# --------------------
name = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:=^20}'.format(name))
# :<20 / :>20 / :^20 = posição da variável e quantidade de bytes que ela vai ocupar
# :=<20 / :=>20 / :^=20 = valor que vai preencher os bytes vazios
print('-'*20)
# --------------------
print('-'*20)
# --------------------
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma resulta em {}, a multiplicação em {}, a divisão em {:.2f}'.format(s, m, d), end=' ')
# :.2f = 2 casas decimais
# end=' ' = juntar o print de cima com o de baixo
# \n = quebrar linha
print('A divisão inteira em {} e a potência em {}'.format(di, e))
print('-'*20)
# --------------------