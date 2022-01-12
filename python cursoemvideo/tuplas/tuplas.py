#tuplas: variáveis compostas imutáveis
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

print(sorted(lanche)) #coloca em ordem e transforma em uma lista

print(lanche[2])     #imprime só o 3º elemento
print(lanche[0:2])   #imprime os elementos 0 e 1
print(lanche[1:])    #imprime a partir do elemento
print(lanche[:3])    #imprime do início até o terceiro elemento
print(lanche[-1])    #imprime o último elemento

tamanhoLanche = len(lanche) #len = função de tamanho
print(tamanhoLanche)

for comida in lanche: #a cada rodagem do laço, o valor que comida recebe é um dos argumentos do lanche
    print(f'Eu vou comer {comida}')
#for com as posições de cada elemento
for cont in range(0, len(lanche)):
    print(f'{lanche[cont]} foi a {cont + 1}ª comida')
    
for pos, comida in enumerate(lanche):
    print(f'{pos + 1}º eu comi {comida}')
    
#o único jeito de mudar uma tupla é apagá-la inteira da memória com o comando del
#exemplo del(lanche)