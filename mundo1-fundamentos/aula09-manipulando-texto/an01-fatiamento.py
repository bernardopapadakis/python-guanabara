# Em python cara byte recebe um número, em ordem crescente a partir do 0.
frase = 'Curso em Vídeo Python'
#        0123456789...
print(frase[9]) # escreve 'V'
print(frase[9:13])# escreva 'Víde'
print(frase[9:21])# escreva 'Vídeo Python'
print(frase[9:21:2])# escreve 'VdoPto
print(frase[:5])# escreve 'Curso'
print(frase[15:])# escreve 'Python'
print(frase[9::3])# escreve 'VePh'

print('-'*40)

# Para escrever na tela textos longos quebrando a linha pode se usar """ dentro do print
print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque quis leo nibh. Donec turpis felis, 
molestie id pellentesque sed, molestie vel ex. Curabitur tincidunt feugiat enim a suscipit. Sed lacus lacus, euismod 
sit amet gravida et, tempus quis purus. Mauris tempus ipsum purus, a auctor justo vestibulum ac. Integer neque metus,
tincidunt in pretium sed, mattis eu metus. Aliquam ornare vulputate interdum. Pellentesque habitant morbi tristique
senectus et netus et malesuada fames ac turpis egestas. Pellentesque a fermentum libero. In venenatis vitae orci id
rutrum. Pellentesque et nulla et nulla tristique scelerisque. Morbi sit amet lectus mauris. Donec eget augue non 
ligula pulvinar molestie sit amet et dui. Aliquam erat volutpat. Nam semper augue sit amet massa iaculis efficitur.
Pellentesque nec lectus nec eros varius commodo eu sit amet arcu.
""")