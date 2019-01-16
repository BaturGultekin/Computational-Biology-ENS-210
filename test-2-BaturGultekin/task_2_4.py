import sys
from alignment import getBasicFinder
from alignment import fastareader


geneDict = fastareader("brca2_alignment_noHumanGap.fa")
out = open('basic.txt', 'w')
consensusKeys = fastareader("consensus.fa")

consensus = str(consensusKeys.values())[14:-3]
listOfSequences = list(geneDict.values())
basicIdentity = getBasicFinder(listOfSequences)

j=0
for i in range(len(consensus)):
    out.write(str(i) +'\t'+ str(basicIdentity[j:j+10])+'\n')
    j+=10