import random
import math


class Individuo(object):

    def __init__(self, tamanhoIndividuo, materialGenetico=None ):
        self.fitness = None
        self.valorDecimal = None
        self.tamanhoIndividuo = tamanhoIndividuo

        if(materialGenetico == None):
            self.valorDecimal = random.randint(-(math.pow(tamanhoIndividuo-1, 2)), math.pow(tamanhoIndividuo-1, 2)-1)
            self.materialGenetico = self.intToBin(self.valorDecimal)
        else:
            self.valorDecimal = self.toDecimal()
            self.materialGenetico = materialGenetico
        
        self.calcularFitness()

    def reproducao(self, indiviuo2):
        filho = []
        for i in range(int(self.tamanhoIndividuo)):
            filho.append(-1)
        for i in range(int(self.tamanhoIndividuo)):
            if i <= int(self.tamanhoIndividuo/2):
                filho[i] = self.materialGenetico[i]
            else:
                filho[i] = indiviuo2.materialGenetico[i]
        return filho

    #Converte um número decimal para um array binário
    def intToBin(self, inteiro):
        strBinario = ""
        binario = bin(inteiro)

        if(binario.startswith('-')):
            strBinario += '1'
        else:
            strBinario += '0'

        strBinario = strBinario + binario.split("b")[1]
        
        return list(strBinario)


    def calcularFitness(self):
        if(self.fitness == None):
            # Função x² + 3x | b² - 4ac = 9 - 4.1.0 = 9
            self.fitness = math.pow(self.valorDecimal, 2) + \
                (3 * self.valorDecimal)

        return self.fitness

    def toDecimal(self):
        if(self.materialGenetico[0] == '1'):
            decimal = "-0b"
        else:
            decimal = "0b"

        materialGeneticoStr = ''
        materialGeneticoStr = decimal + "".join(self.materialGenetico[1:])
        valorDecimal = int(materialGeneticoStr, 2)

        return self.valorDecimal

    def fazerMutacao(self):
        print("Indivíduo: " + str(self.materialGenetico))

        # Sorteia um gene do indivíduo e inverte seu valor
        posicaoGene = random.randint(0, len(self.materialGenetico)-1)
        gene = self.materialGenetico[posicaoGene]
        print("Gene sorteado: " + str(gene))

        # Altera o gene (invertendo seu valor) e o coloca novamente no indiviuo
        novoGene = '0' if gene == '1' else '1'
        self.materialGenetico[posicaoGene] = novoGene
        self.valorDecimal = toDecimal()
        print("Indivíduo mutado: " + str(self.materialGenetico))

