import math
import matplotlib.pyplot as plt

from Populacao import Populacao

TAMANHO_INDIVIDUO = 8
TAMANHO_POPULACAO = 100

# Função resposável por definir a função matemática que sera usada no algoritmo
def f(x):
  return 5*x**2 + 50*x - 20                     # 5x² + 50x - 20                
  # return x**3 - 4*x**3 + 4*x**2 + 10            # x³ - 4x³ + 4x² + 10
  # return math.cos(3*x) + 3                      # cos(3*x) + 3

plt.title('Gráfico do Fitness das gerações')
plt.xlabel('Geração')
plt.ylabel('Fitness')
                                                                               
# inicializacao da populacao parametros: (TAMANHO_POPULACAO, TAMANHO_INDIVIDUO, POSSUI_MINIMO, FUNCAO_MATEMATICA)
populacao = Populacao(TAMANHO_POPULACAO, TAMANHO_INDIVIDUO, False, f)
populacao.inicializar()
populacao.arrMelhoresIndividuoes.append(populacao.melhorIndividuo.fitness)

while(populacao.contadorGeracao < 300):

  populacao.calcularFitness()

  populacao.selecao(0.7) # o percentual se refere a quantidade de individuos que sobreviverao à selecao

  populacao.reproducao(0.46) # o percentual se refere a quantidade de novos individuos gerados

  populacao.arrMelhoresIndividuoes.append(populacao.melhorIndividuo.fitness)

  populacao.mutacao(0.02) # o percentual se refera a chance da mutação acontecer

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