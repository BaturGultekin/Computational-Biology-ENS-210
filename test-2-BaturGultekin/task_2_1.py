from alignment import fastareader

geneDict = fastareader("brca2_alignment.fa")
out = open('brca2_alignment_noHumanGap.fa', 'w')

listGeneDict = list(geneDict.values())
listKeys = list(geneDict.keys())
numElementsInList= len(listGeneDict)
target = str(geneDict.get(
    'NP_000050.2_breast_cancer_type_2_susceptibility_protein_[Homo_sapiens]'))
    
count =0
for i in range(len(target)):
    if target[i]=='-':
        for j in range (numElementsInList):
            listGeneDict[j] = listGeneDict[j][:(i-count)] + listGeneDict[j][(i+1-count):]
        count +=1
    
for i in range(len(geneDict.keys())):
    out.write('>'+str(listKeys[i])+'\n'+ str(listGeneDict[i])+ '\n')
