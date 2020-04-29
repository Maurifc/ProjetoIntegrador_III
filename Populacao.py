from Individuo import Individuo
import random
import sys

class Populacao(object):

    def __init__(self, tamanhoPopulacao, tamanhoIndividuo):
        self.populacao = []
        self.contadorGeracao = 1
        self.geracoes = [1]
        self.fitnessMedioDasGeracoes = []
        self.melhorIndividuo = None
        self.tamanhoPopulacao = tamanhoPopulacao
        self.tamanhoIndividuo = tamanhoIndividuo

    def inicializar(self):
        for i in range(self.tamanhoPopulacao):
            individuo = Individuo(self.tamanhoIndividuo)
            self.populacao.append(individuo)
            print(individuo.materialGenetico)

        self.fitnessMedioDasGeracoes.append(self.calcularFitnessMedio())
        self.selecao()
    
    def calcularFitnessMedio(self):
        fitnessTotal = 0
        for i in range(self.tamanhoPopulacao):
            fitnessTotal += self.populacao[i].calcularFitness()
        
        return fitnessTotal / self.tamanhoPopulacao
    
    def mutacao(self):
        #Sorteia um indivíduo da população
        posicaoIndividuo = random.randint(0, len(self.populacao)-1)
        print("Posicao Indiviuo:" + str(posicaoIndividuo))
        self.populacao[posicaoIndividuo].fazerMutacao()

    def reproducao(self, taxaReproducao):
        inicio = self.tamanhoPopulacao - 1
        fim = ((self.tamanhoPopulacao) - 1) - int(self.tamanhoPopulacao * (taxaReproducao/100))
        for i in range(inicio, fim, -2):
            novoIndividuo = Individuo(self.tamanhoIndividuo)
            novoIndividuo.materialGenetico = self.populacao[i].reproducao(self.populacao[i-1])
            self.populacao.append(novoIndividuo)
            self.tamanhoPopulacao = self.tamanhoPopulacao + 1

        #Incrementa o contador de geracoes
        self.contadorGeracao += 1
        #Coloca mais uma geracao no array de geracoes e seu respectivo fitness médio no array 'fitness'
        self.geracoes.append(self.contadorGeracao)
        self.fitnessMedioDasGeracoes.append(self.calcularFitnessMedio())

        self.exibirMaterialGenetico()

    def selecao(self):
        self.populacao = sorted(self.populacao, key=lambda Individuo: Individuo.fitness) #Ordena do pior para o melhor indivíduo
        self.melhorIndividuo = self.populacao[len(self.populacao)-1] #Pega o melhor indivíduo da geração

    def adicionarDescendente(self, descendente):
        menorFitness = sys.float_info.max

        for indice,individuo in enumerate(self.populacao):
            if (individuo.calcularFitness() < menorFitness):
                indiceMenorFitness = indice
    
        self.populacao[indiceMenorFitness] = descendente

    def exibirMaterialGenetico(self):
        for i in range(self.tamanhoPopulacao):
            print(self.populacao[i].materialGenetico)