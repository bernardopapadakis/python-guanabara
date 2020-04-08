"""
    Para análisar uma frase podemos usar as funções:
- len
- .count
- .find
"""
frase = 'Curso em Vídeo Python'
print(len(frase)) # mostra quantos bytes tem
print(frase.count('o')) # mostra quantas vezes a str que vc colocar entre ( ) aparece
print(frase.count('o', 0, 13))# igual anterior, porém com a limitação do byte 0, ao 13 no caso
print(frase.find('deo'))# fala a poscição da str dentro dos ( )
print('Curso' in frase)# para saber se a str escrita está dentro da variável depois do in