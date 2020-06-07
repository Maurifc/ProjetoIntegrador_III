from Individuo import Individuo
import random
import sys
import math


class Populacao(object):

    def __init__(self, tamanhoPopulacao, tamanhoIndividuo):
        self.populacao = []
        self.contadorGeracao = 1
        self.geracoes = [1]
        self.fitnessMedioDasGeracoes = [0]

        self.arrMelhoresIndividuoes = []

        self.melhorIndividuo = Individuo(tamanhoIndividuo)
        self.melhorIndividuo.fitness = None

        self.tamanhoPopulacao = tamanhoPopulacao
        self.tamanhoIndividuo = tamanhoIndividuo

    def inicializar(self):
        for i in range(self.tamanhoPopulacao):
            individuo = Individuo(self.tamanhoIndividuo)

            # insere no array de melhores individuos caso o indivio seja melhor que o melhor atual
            if self.melhorIndividuo.fitness == None or individuo.fitness < self.melhorIndividuo.fitness:
                self.melhorIndividuo = individuo

            self.populacao.append(individuo)

    def calcularFitness(self):
        fitnessTotal = 0
        for i in range(self.tamanhoPopulacao):
            fitnessTotal += self.populacao[i].calcularFitness()

        fitnessMedio = fitnessTotal / self.tamanhoPopulacao

        self.fitnessMedioDasGeracoes.append(fitnessMedio)

        return fitnessMedio

    def mutacao(self):
        # Sorteia um indivíduo da população
        posicaoIndividuo = random.randint(0, len(self.populacao)-1)
        # print("Posicao Indiviuo Mutado:" + str(posicaoIndividuo))
        self.populacao[posicaoIndividuo].fazerMutacao()

    def reproducao(self):
        i = 0
        i2 = 0
        while(i == i2):
            i = random.randint(0, self.tamanhoPopulacao - 1)
            i2 = random.randint(0, self.tamanhoPopulacao - 1)

        novoIndividuo = self.populacao[i].reproducao(self.populacao[i2])

        # insere no array de melhores individuos caso o indivio seja melhor que o melhor atual
        if self.melhorIndividuo.fitness == None or novoIndividuo.fitness < self.melhorIndividuo.fitness:
            self.melhorIndividuo = novoIndividuo

        self.populacao.append(novoIndividuo)
        self.tamanhoPopulacao += 1

    def selecao(self):
        fitnessMaximo = sum([c.fitness for c in self.populacao])
        fitnessSelecionado = random.uniform(0, fitnessMaximo)
        fitnessAtual = 0
        for individuo in self.populacao:
            fitnessAtual += individuo.fitness
            if fitnessAtual > fitnessSelecionado:
                self.populacao.remove(individuo)
                self.tamanhoPopulacao -= 1;
                return individuo

    def adicionarDescendente(self, descendente):
        menorFitness = sys.float_info.max

        for indice,individuo in enumerate(self.populacao):
            if (individuo.calcularFitness() < menorFitness):
                indiceMenorFitness = indice
    
        self.populacao[indiceMenorFitness] = descendente

    def exibirMaterialGenetico(self):
        for i in range(self.tamanhoPopulacao):
            print(self.populacao[i].toDecimal())
