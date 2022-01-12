# Crie uma lista de 5 números informados pelo usuário que não podem se repetir e que esteja em ordem crescente sem utilizar a função sort
cont = 0
listaNumeros = list()
while cont != 5:
    num = int(input('Digite um número inteiro: '))
    if num not in listaNumeros:
        listaNumeros.append(num)
    else:
        print(f'O número {num} já foi inserido na lista, tente novamente')
        cont -= 1
    cont += 1

for n in range(0,len(listaNumeros)):
    num = listaNumeros[n]
    for c, v in enumerate(listaNumeros):
        if num > v:
            listaNumeros.remove(num)
            listaNumeros.insert(c, num)

cont2 = 0
while cont2 != len(listaNumeros):
    for i in range(0, (len(listaNumeros)-1)):
        if listaNumeros[i] > listaNumeros[i+1]:
            listaNumeros.append(listaNumeros[i])
            listaNumeros.pop(i)
    cont2 += 1

print(f'A lista gerada foi {listaNumeros}')