#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular

compras = ('Banana', 0.75, 'Chocolate', 2.3, 'Borracha', 4.2, 'Apontador', 3.5, 'Álbum KPOP', 210)
stringCompras = 'LISTA DE COMPRAS'
stringCompras = stringCompras.center(33)
print('-'*33)
print(stringCompras)
print('-'*33)

for c in range(0, len(compras), 2):
    print(f'{compras[c]:.<25}' + f'R${compras[c+1]:>5}')