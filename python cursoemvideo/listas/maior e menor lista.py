#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

numeros = list()

for c in range(0,5):
    num = int(input('Digite um número: '))
    numeros.append(num)
    
maior = numeros[0]
menor = numeros[0]

for r in range(0, len(numeros)):
    if numeros[r] > maior:
        maior = numeros[r]
    if numeros[r] < menor:
        menor = numeros[r]
   
print('A lista informada foi', end=" ")        
for c in numeros:
    print(f'{c}', end=" ")
    
print(f'\n O maior número informado foi {maior} e o menor foi {menor}')