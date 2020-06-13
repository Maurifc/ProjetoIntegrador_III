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
populacao = Populacao(TAMANHO_POPULACAO, TAMANHO_INDIVIDUO, True)
populacao.inicializar()
populacao.arrMelhoresIndividuoes.append(populacao.melhorIndividuo.fitness)

while(populacao.contadorGeracao < 400):

  # calculo do fitness
  populacao.calcularFitness()

  # selecao
  populacao.selecao(0.7) # a porcentagem se refere a quantidade de individuos que sobreviverao à selecao

  # reproducao
  populacao.reproducao(0.46) # a porcentagem se refere a quantidade de individuos que farao a reproducao

  populacao.arrMelhoresIndividuoes.append(populacao.melhorIndividuo.fitness)
  populacao.mutacao()

  populacao.contadorGeracao += 1
  populacao.geracoes.append(populacao.contadorGeracao)

  print('Geração -> ' + str(populacao.contadorGeracao))
  print('melhor indivíduo => ' + str(populacao.melhorIndividuo.valorDecimal))
  print('melhor indivíduo fitness => ' + str(populacao.melhorIndividuo.fitness))
  print('tamanho populacao => ' + str(len(populacao.populacao)))
  print('-----------------------------------------------------------------------')


#Exibição do gráfico
plt.plot(populacao.geracoes, populacao.fitnessMedioDasGeracoes)
plt.plot(populacao.geracoes, populacao.arrMelhoresIndividuoes)
plt.show()