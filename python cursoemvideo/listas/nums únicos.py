#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

print('CRIE UMA LISTA DE NÚMEROS')

numNovo = int(input('Digite um número:'))
listaNumeros = list()
listaNumeros.append(numNovo)
continuar = input('Deseja continuar? (sim/não): ')

while continuar == 'sim':
    numNovo = int(input('Digite um número:'))
    if numNovo not in listaNumeros:
        listaNumeros.append(numNovo)
    else:
        print('Este número já está na lista')
    continuar = input('Deseja continuar? (sim/não): ')
        
listaNumeros.sort()

print(f'A lista digitada foi {listaNumeros}')