#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:A) Quantas vezes apareceu o valor 9.B) Em que posição foi digitado o primeiro valor 3.C) Quais foram os números pares.

print('Digite quatro números:')
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

numeros = (num1, num2, num3, num4)

print(f'Foram encontrados {numeros.count(9)} números 9 na tupla')

if 3 in numeros:
    print(f'O número 3 apareceu na posição {numeros.index(3)+1}')

print('Os números pares da tupla são:')
for num in numeros:
    if num%2 == 0:
        print(num)