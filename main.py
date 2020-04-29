import random
import math
from Populacao import Populacao
import graficoFitnessMedio as grafico

TAMANHO_INDIVIDUO = 5
TAMANHO_POPULACAO = 100

#inicializacao da populacao
populacao = Populacao(TAMANHO_POPULACAO, TAMANHO_INDIVIDUO)
populacao.inicializar()

for i in range(100):
  populacao.calcularFitnessMedio()
  populacao.selecao()
  populacao.reproducao(70)
  populacao.mutacao()
  grafico.plotar(populacao)