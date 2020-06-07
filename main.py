import _thread
import random
import math
from Populacao import Populacao

import matplotlib.pyplot as plt

TAMANHO_INDIVIDUO = 8
TAMANHO_POPULACAO = 100

# inicializacao do grafico
plt.title('Gráfico do Fitness das gerações')
plt.xlabel('Geração')
plt.ylabel('Fitness')
plt.colormaps

# inicializacao da populacao
populacao = Populacao(TAMANHO_POPULACAO, TAMANHO_INDIVIDUO)
populacao.inicializar()
populacao.arrMelhoresIndividuoes.append(populacao.melhorIndividuo.fitness)

# while(populacao.melhorIndividuo.toDecimal() != -2.25):
while(populacao.contadorGeracao < 300):
  populacao.calcularFitness()

  for i in range(20):
    populacao.selecao()

  for i in range(30):
    populacao.reproducao()

  populacao.arrMelhoresIndividuoes.append(populacao.melhorIndividuo.fitness)
  populacao.mutacao()

  populacao.contadorGeracao += 1
  populacao.geracoes.append(populacao.contadorGeracao)

  print('Geração -> ' + str(populacao.contadorGeracao))
  print('melhor indivíduo => ' + str(populacao.melhorIndividuo.valorDecimal))
  print('melhor indivíduo fitness => ' + str(populacao.melhorIndividuo.fitness))


#Exibição do gráfico
plt.plot(populacao.geracoes, populacao.fitnessMedioDasGeracoes)
plt.plot(populacao.geracoes, populacao.arrMelhoresIndividuoes)
plt.show()