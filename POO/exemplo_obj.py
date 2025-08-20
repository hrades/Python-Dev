# Trabalhando com dicionários
def cria_tv(ano, marca, valor, n_canais):
    return {'ano':ano, 'marca':marca, 'valor':valor, 'n_canais':n_canais}

def aumentar_canais(tv,canal):
    tv['n_canais'] += canal

tv = cria_tv(2019, 'LG', 2800.0, 20)
print(tv)

aumentar_canais(tv,5)
print('Nova quantidade de canais: ' + str(tv['n_canais']))

class Televisao():
    def __init__(self, ano, marca, valor, n_canais):
        self._ano = ano
        self._marca = marca
        self._valor = valor
        self._n_canais = n_canais
    
    def aumentar_canais(self, quantidade):
        self._n_canais += quantidade 

tv_1 = Televisao(2022, 'Samsung', 3599.99, 50)
tv_1.aumentar_canais(100)
print(tv_1._n_canais)

tv_2 = Televisao(2025, 'Phillips', 4999.99, 100)

