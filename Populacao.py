from Individuo import Individuo
import random
import sys
import math


class Populacao(object):

    def __init__(self, tamanhoPopulacaoInicial, tamanhoIndividuo, isMinimo):
        self.isMinimo = isMinimo

        self.populacao = []
        self.contadorGeracao = 1
        self.geracoes = [1]
        self.fitnessMedioDasGeracoes = [0]

        self.arrMelhoresIndividuoes = []

        self.melhorIndividuo = Individuo(tamanhoIndividuo)
        self.melhorIndividuo.fitness = None

        self.tamanhoPopulacaoInicial = tamanhoPopulacaoInicial
        self.tamanhoIndividuo = tamanhoIndividuo

    def inicializar(self):
        for i in range(self.tamanhoPopulacaoInicial):
            individuo = Individuo(self.tamanhoIndividuo)

            # insere no array de melhores individuos caso o indivio seja melhor que o melhor atual
            if self.isMinimo:
                if self.melhorIndividuo.fitness == None or individuo.fitness < self.melhorIndividuo.fitness:
                    self.melhorIndividuo = individuo
            else:
                if self.melhorIndividuo.fitness == None or individuo.fitness > self.melhorIndividuo.fitness:
                    self.melhorIndividuo = individuo

            self.populacao.append(individuo)

    def calcularFitness(self):
        fitnessTotal = 0
        for i in range(len(self.populacao)):
            fitnessTotal += self.populacao[i].calcularFitness()

        fitnessMedio = fitnessTotal / len(self.populacao)

        self.fitnessMedioDasGeracoes.append(fitnessMedio)

        return fitnessMedio

    def mutacao(self):
        # Sorteia um indivíduo da população
        posicaoIndividuo = random.randint(0, len(self.populacao)-1)
        # print("Posicao Indiviuo Mutado:" + str(posicaoIndividuo))
        self.populacao[posicaoIndividuo].fazerMutacao()

    def reproducao(self, percent):
        # contador de individuos que serao reproduzidos
        count = int(len(self.populacao) * percent)

        for i in range(count):
            ind1: Individuo = None
            ind2: Individuo = None

            # seleciona os individuos para o cruzamento cetificando-se que
            # o indivíduo 1 e o individuo 2 não sejam o mesmo individuo
            ind1 = self.torneio(1)[0]
            ind2 = self.torneio(1)[0]

            # reproducao
            novoIndividuo = ind1.reproducao(ind2)

            if self.isMinimo:
                if self.melhorIndividuo.fitness == None or novoIndividuo.fitness < self.melhorIndividuo.fitness:
                    self.melhorIndividuo = novoIndividuo
            else:
                if self.melhorIndividuo.fitness == None or novoIndividuo.fitness > self.melhorIndividuo.fitness:
                    self.melhorIndividuo = novoIndividuo

            # adicao do individo gerado à populacao
            self.populacao.append(novoIndividuo)

    def selecao(self, percent):  # selecao por toneio
        # contador de individuos que serao selecionados
        count = int(len(self.populacao) * percent)

        self.populacao = self.torneio(count)

    def torneio(self, count):
        # array de individuos selecionados
        selecionados = []

        for i in range(count):
            ind1 = None
            ind2 = None
            ind3 = None

            # escolhe as posicoes do toneio se certificando que elas nao se repitam
            while True:
                ind1 = random.randint(0, len(self.populacao) - 1)
                ind2 = random.randint(0, len(self.populacao) - 1)
                ind3 = random.randint(0, len(self.populacao) - 1)
                if ind1 != ind2 and ind2 != ind3:
                    break

            fitnessInd1 = self.populacao[ind1].fitness
            fitnessInd2 = self.populacao[ind2].fitness
            fitnessInd3 = self.populacao[ind3].fitness

            # selecao do mais apto no toneio
            if self.isMinimo:
                if fitnessInd1 < fitnessInd2 and fitnessInd1 < fitnessInd3:
                    selecionados.append(self.populacao[ind1])
                elif fitnessInd2 < fitnessInd1 and fitnessInd2 < fitnessInd3:
                    selecionados.append(self.populacao[ind2])
                else:
                    selecionados.append(self.populacao[ind3])
            else:
                if fitnessInd1 > fitnessInd2 and fitnessInd1 > fitnessInd3:
                    selecionados.append(self.populacao[ind1])
                elif fitnessInd2 > fitnessInd1 and fitnessInd2 > fitnessInd3:
                    selecionados.append(self.populacao[ind2])
                else:
                    selecionados.append(self.populacao[ind3])

        return selecionados

    def adicionarDescendente(self, descendente):
        menorFitness = sys.float_info.max

        for indice, individuo in enumerate(self.populacao):
            if (individuo.calcularFitness() < menorFitness):
                indiceMenorFitness = indice

        self.populacao[indiceMenorFitness] = descendente

    def exibirMaterialGenetico(self):
        for i in range(len(self.populacao)):
            print(self.populacao[i].toDecimal())
