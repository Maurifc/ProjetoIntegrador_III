import random
import math
from Populacao import Populacao
import graficoFitnessMedio as grafico

TAMANHO_INDIVIDUO = 5
TAMANHO_POPULACAO = 100

#inicializacao da populacao
populacao = Populacao(TAMANHO_POPULACAO, TAMANHO_INDIVIDUO)
populacao.inicializar()

# while(populacao.melhorIndividuo.toDecimal() != -2.25):
for i in range(0,100):
    populacao.calcularFitnessMedio()
    populacao.selecao()
    populacao.reproducao(50)
    populacao.mutacao()

grafico.plotar(populacao)