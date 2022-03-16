#Objetivo: Fazer um programa que resolva o algoritmo da bisseção
#Autor: Heloísa Rades de Souza      Data:16/03/2022

#importar bibliotecas
#import numpy as np
import math

print('''Esta é uma calculadora de raízes pelo método da bisseção
Sua precisão é de 4 casas decimais''')


#Ler intervalo e erro informados pelo usuário
a = float(input('Digite o início do intervalo: '))
b = float(input('Digite o final do intervalo: '))
erro = float(input('Digite o erro: '))

funcao = '{x**2 - 3}'
#Função para calcular x-barra (média)
def media(a,b):
    med = (a+b)/2
    return med

#Ler e calcular a função
def f(x):
    return x**2 - 3

#Calcular número de iterações  --  não está funcionando
#n_iteracoes = (np.log(a-b) - np.log(erro))/np.log(2)
#k = np.ceil(n_iteracoes)
#print(f'O número mínimo de iterações calculado foi {k}')

if f(a)*f(b) < 0:
    while True:
       x0 = media(a,b)
       
       print(f'''a = {a:.4f} | b = {b:.4f} | x = {x0:.4f} | f(a) = {f(a):.4f} | f(x) = {f(x0):.4f} | sinal = {f(a)*f(b):.4f} | E = {(b-a):.4f}''')
       
       if (b-a) < erro:
           print(f'{x0:.4f} é a raiz da função')
           break
       else:
           if f(a)*f(x0) > 0:
               a = x0
           else:
               b = x0
else:
    print('Não há raíz para este intervalo')
