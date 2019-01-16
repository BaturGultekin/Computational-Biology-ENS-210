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

#### I did not use any necessary functions for Task_2_1, if you check task_2_1.py you will see that there is no function needed for my algorithm

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

def identityOfConsensus(listOfSequences):
    identityRatio = ''
    countGap = 0
    for position in range(len(listOfSequences[0])):
        chardict = dict()
        for currentSeq in range(len(listOfSequences)):
            char = listOfSequences[currentSeq][position]
            if char !='-':
                if char in chardict:
                    chardict[char] += 1
                else:
                    chardict[char] = 1
            else:
                countGap+=1
        identityRatio += (str("{0:.8f}".format(((max(chardict.values()))/(982-countGap)))))
        countGap=0
    return identityRatio

def getBasicFinder(listOfSequences):
    identityRatio = ''
    countGap = 0
    countKHR= 0
    for position in range(len(listOfSequences[0])):
        chardict = dict()
        for currentSeq in range(len(listOfSequences)):
            char = listOfSequences[currentSeq][position]
            if char !='-':
                if char in chardict:
                    chardict[char] += 1
                else:
                    chardict[char] = 1
            else:
                countGap+=1

        if chardict.get('K') or chardict.get('R') or chardict.get('H'):
            countKHR+=1
        
        identityRatio += (str("{0:.8f}".format((countKHR)/(982-countGap))))
        countGap=0
        countKHR=0
    return identityRatio

# There are some useful information for "Calculating a consensus sequence", I used some information when I was writing this code.
#http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec:summary_info
#http://www.cbs.dtu.dk/courses/27610/example09.html