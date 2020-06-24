import random
import math

class Individuo(object):

    def __init__(self, tamanhoIndividuo, f,materialGenetico=None):
        self.f = f
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
            self.valorDecimal = self.binToDec()
        
        self.calcularFitness()

    def reproducao(self, indiviuo2):
        posCruzamento = random.randint(0, self.tamanhoIndividuo)
        mGeneticoNovoIndividuo = self.materialGenetico[0:posCruzamento]
        
        for i in range(posCruzamento, self.tamanhoIndividuo):
                mGeneticoNovoIndividuo.append(indiviuo2.materialGenetico[i])

        if(len(mGeneticoNovoIndividuo) < self.tamanhoIndividuo):
            raise Exception("erro na reproducao")

        return Individuo(self.tamanhoIndividuo, self.f,mGeneticoNovoIndividuo)

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

    #convert um array binário para um número decimal
    def binToDec(self):
        if(self.materialGenetico[0] == '1'):
            decimal = "-0b"
        else:
            decimal = "0b"

        materialGeneticoStr = ''
        materialGeneticoStr = decimal + "".join(self.materialGenetico[1:])
        self.valorDecimal = int(materialGeneticoStr, 2)

        return self.valorDecimal

    def calcularFitness(self):
        self.fitness = self.f(self.valorDecimal)

        return self.fitness

    def fazerMutacao(self):
        
        # Sorteia um gene do indivíduo e inverte seu valor
        posicaoGene = random.randint(0, self.tamanhoIndividuo-1)
        gene = self.materialGenetico[posicaoGene]
        #print("Gene sorteado: " + str(gene))

        # Altera o gene (invertendo seu valor) e o coloca novamente no indiviuo
        novoGene = '0' if gene == '1' else '1'
        self.materialGenetico[posicaoGene] = novoGene
        self.valorDecimal = self.binToDec()
        
        print("Indivíduo mutado: " + str(self.materialGenetico))

