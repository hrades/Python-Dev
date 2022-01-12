#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#Os 5 primeiros times; Os últimos 4 colocados; Times em ordem alfabética; Em que posição está o time da Chapecoense.

timesBrasileirao = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print(f'Os cinco primeiros times são: {timesBrasileirao[0:5]} \n')

print(f'Os últimos quatro colocados são: {timesBrasileirao[-4:]} \n')

timesAlfabetica = sorted(timesBrasileirao)
for times in timesAlfabetica:
    print(times)
print('\n')

posicaoChapecoense = timesBrasileirao.index('Chapecoense') + 1
print(f'A Chapecoense é a {posicaoChapecoense}ª colocada')
