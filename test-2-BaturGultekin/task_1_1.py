#FastaReader
def fastareader(filename):
    seqDict = {}
    filein = open(filename, 'r')
    for line in filein:
        if line[0] == '>':
            k = line[1:]
            k = k.strip("\n")
            seqDict[k] = ""
        else:
            seqDict[k] += line.strip("\n")

    return seqDict


geneDict = fastareader("proopiomelanocortin.fa")
out = open('proopiomelanocortin_CpG.txt', 'w')

stringGene = str(geneDict.values())[14:-3]


for j in range(0,(len(stringGene)-100)):
    numOfC = stringGene.count("C", j, (j+100))
    numOfG = stringGene.count("G", j, (j+100))
    numOfCG = stringGene.count("CG", j, (j+100))

    out.write(str(j)+'\t' +'\t'+
              str((numOfCG*100)/(numOfC*numOfG)) + '\n')

#Referance for the count function https://www.programiz.com/python-programming/methods/string/count