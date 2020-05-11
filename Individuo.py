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
            if(len(materialGenetico) < tamanhoIndividuo):
                raise Exception("Tamanho do material genético informado é inferior ao tamanho do indivíuo estabelecido.")

            self.materialGenetico = materialGenetico
            self.valorDecimal = self.toDecimal()
        
        self.calcularFitness()

    def reproducao(self, indiviuo2):
        posCruzamento = int(self.tamanhoIndividuo/2)
        mGeneticoNovoIndividuo = self.materialGenetico[0:posCruzamento]

        for i in range(posCruzamento, self.tamanhoIndividuo):
                mGeneticoNovoIndividuo.append(indiviuo2.materialGenetico[i])

        if(len(mGeneticoNovoIndividuo) < self.tamanhoIndividuo):
            raise Exception("erro na reproducao")

        return Individuo(self.tamanhoIndividuo, mGeneticoNovoIndividuo)

    #Converte um número decimal para um array binário
    def intToBin(self, inteiro):
        strBinario = ""
        binario = bin(inteiro)

        strBinario = strBinario + binario.split("b")[1]

        strBinarioFormatado = strBinario.zfill(self.tamanhoIndividuo-1)

        if(binario.startswith('-')):
            strBinarioFormatado = '1' + strBinarioFormatado
        else:
            strBinarioFormatado = '0' + strBinarioFormatado
            
        return list(strBinarioFormatado)


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
        self.valorDecimal = int(materialGeneticoStr, 2)

        return self.valorDecimal

    def fazerMutacao(self):
        print("Indivíduo: " + str(self.materialGenetico))

        # Sorteia um gene do indivíduo e inverte seu valor
        posicaoGene = random.randint(0, self.tamanhoIndividuo-1)
        gene = self.materialGenetico[posicaoGene]
        print("Gene sorteado: " + str(gene))

        # Altera o gene (invertendo seu valor) e o coloca novamente no indiviuo
        novoGene = '0' if gene == '1' else '1'
        self.materialGenetico[posicaoGene] = novoGene
        self.valorDecimal = self.toDecimal()
        print("Indivíduo mutado: " + str(self.materialGenetico))

