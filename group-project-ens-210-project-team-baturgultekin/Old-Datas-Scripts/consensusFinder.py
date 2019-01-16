import sys

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
    
def consensusfinder(listOfSequences):
    consensus = ''
    for position in range(len(listOfSequences[0])):
        chardict = dict()
        for currentSeq in range(len(listOfSequences)):
            if listOfSequences[currentSeq][position] !='-':
                char = listOfSequences[currentSeq][position]
                if char in chardict:
                    chardict[char] += 1
                else:
                    chardict[char] = 1
        consensus += sorted(chardict.keys(), reverse=True, key=chardict.get)[0]
    return consensus


geneDict = fastareader("TPD52-aligned.fas")
out = open('consensusTPD52.fa', 'w')
listOfSequences = list(geneDict.values())
consensusTPD52 = consensusfinder(listOfSequences)

out.write('>TPD52 consensus sequence'+'\n'+consensusTPD52)
