#listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

from random import randint

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)

lanche[3]='sorvete' #substituir um elemento existente na lista
print(lanche)

lanche.append('cookie') #adiciona no final
print(lanche)

lanche.insert(2, 'cachorro-quente') #cria um novo elemento na posição existente e rearranja os seguintes uma posição a mais
print(lanche)

#3 métodos para apagar elemenentos
del lanche[0]
lanche.pop(2) #pode ser utilizado como .pop() para apagar o último elemento
lanche.remove('cookie') #remove o elemento sem ser por índice - melhor utilizar um if para conferir se há na lista para previnir um erro - remove somente o primeiro que acha
print(lanche)

#criar listas através de ranges
valores=list()
for v in range (0,5):
    valores.append(randint(0,10))
print(valores)

valores.sort() #organizar números em ordem crescente
print(valores)

valores.sort(reverse=True) #organizar em ordem decrescente
print(valores)

#--------PARTE PRÁTICA------------
numeros = [2,5,9,1]
numeros[2] = 7
numeros.pop()
numeros.append(14)
numeros.sort()
numeros.insert(0,2)
print(f'A lista 1 possui {len(numeros)} elementos')
if 4 in numeros:
    numeros.remove(4)
else:
    print('Não achei o número 4 na lista 1')

for c, n in enumerate(numeros):
    print(f'Na posição {c} encontrei o número {n}')
print('Cheguei ao final da primeira lista')

valores = numeros[:] #a lista valores recebe a lista numeros sem estarem conectadas
valores.pop(0)

for v in valores:
    print(f'{v} ', end='')
    
print(f'\n Lista 1 = {numeros}\n Lista 2 = {valores}')