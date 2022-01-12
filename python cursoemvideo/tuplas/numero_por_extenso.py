#escrever um número por extenso um número usando tuplas

numeroExtenso = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
numeroAlgarismo = 0

while (numeroAlgarismo<1 or numeroAlgarismo>20):
    numeroAlgarismo = int(input('Digite um número inteiro entre 1 e 20: '))

for numero in range(0, len(numeroExtenso)):
    if numero + 1 == numeroAlgarismo:
        print(numeroExtenso[numero])