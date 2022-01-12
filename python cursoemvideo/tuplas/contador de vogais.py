# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

twice = ('Nayeon', 'Jeongyeon', 'Momo', 'Sana', 'Jihyo', 'Mina', 'Dahyun', 'Chaeyoung', 'Tzuyu')

listaVogais = list()

for t in twice:
    membro = t.lower()
    for m in membro:
        if m in 'aeiou':
            listaVogais.append(m)
    print(f'As vogais de {t} são {listaVogais}')
    listaVogais.clear()
