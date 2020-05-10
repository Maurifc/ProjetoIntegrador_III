import _thread
import random
import math
from Populacao import Populacao

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

TAMANHO_INDIVIDUO = 8
TAMANHO_POPULACAO = 10000

style.use('fivethirtyeight')

# inicializacao do grafico
plt.title('Gráfico do Fitness das gerações')
plt.xlabel('Geração')
plt.ylabel('Fitness médio')
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# inicializacao da populacao
populacao = Populacao(TAMANHO_POPULACAO, TAMANHO_INDIVIDUO)
populacao.inicializar()

def animate(i):
  ax1.clear()
  ax1.plot(populacao.geracoes, populacao.fitnessMedioDasGeracoes)


ani = animation.FuncAnimation(fig, animate, interval=1000)
_thread.start_new_thread(plt.show, ())

# while(populacao.melhorIndividuo.toDecimal() != -2.25):
while(1):
  populacao.calcularFitnessMedio()
  populacao.selecao()
  populacao.reproducao(70)
  populacao.mutacao()
