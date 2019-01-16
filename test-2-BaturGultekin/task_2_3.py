import sys
from alignment import identityOfConsensus
from alignment import fastareader


geneDict = fastareader("brca2_alignment_noHumanGap.fa")
out = open('identity.txt', 'w')
consensusKeys = fastareader("consensus.fa")

consensus = str(consensusKeys.values())[14:-3]
listOfSequences = list(geneDict.values())
consensusIdentity = identityOfConsensus(listOfSequences)

j=0
for i in range(len(consensus)):
    out.write(str(i) +'\t'+ str(consensusIdentity[j:j+10])+'\n')
    j+=10