#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

listaNumeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

#print(listaNumeros)

maior = listaNumeros[0]
menor = listaNumeros[0]

for num in listaNumeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
        
print(f'O maior número sorteado da lista {listaNumeros} é {maior} e o menor é {menor}')