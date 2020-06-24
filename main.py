import math
import matplotlib.pyplot as plt

from Populacao import Populacao

TAMANHO_INDIVIDUO = 8
TAMANHO_POPULACAO = 100

def f(x):
  return 5*x**2 + 10*x - 10                     # 5x² + 10x - 10                
  # return x**3 - 4*x**3 + 4*x**2 + 10            # x³ - 4x³ + 4x² + 10
  # return math.cos(3*x) + 3                      # cos(3*x) + 3
  # return 8*x**2 + 2*math.cos(5*x) + 12*x + 12     # 8x² + 2 cos(5x) + 12x + 12

# inicializacao do grafico
plt.title('Gráfico do Fitness das gerações')
plt.xlabel('Geração')
plt.ylabel('Fitness')
                                                                               
# inicializacao da populacao parametros: (TAMANHO_POPULACAO, TAMANHO_INDIVIDUO, POSSUI_MINIMO, FUNCAO_MATEMATICA)
populacao = Populacao(TAMANHO_POPULACAO, TAMANHO_INDIVIDUO, True, f)
populacao.inicializar()
populacao.arrMelhoresIndividuoes.append(populacao.melhorIndividuo.fitness)

while(populacao.contadorGeracao < 20):

  populacao.calcularFitness()

  populacao.selecao(0.7) # a porcentagem se refere a quantidade de individuos que sobreviverao à selecao

  populacao.reproducao(0.46) # a porcentagem se refere a quantidade de individuos que farao a reproducao

  populacao.arrMelhoresIndividuoes.append(populacao.melhorIndividuo.fitness)
  populacao.mutacao(0.02)

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