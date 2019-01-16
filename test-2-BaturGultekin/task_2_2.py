import sys
from alignment import fastareader
from alignment import consensusfinder

geneDict = fastareader("brca2_alignment_noHumanGap.fa")
out = open('consensus.fa', 'w')

listOfSequences = list(geneDict.values())
consensus = consensusfinder(listOfSequences)

out.write('>BRCA2 consensus sequence'+'\n'+consensus)