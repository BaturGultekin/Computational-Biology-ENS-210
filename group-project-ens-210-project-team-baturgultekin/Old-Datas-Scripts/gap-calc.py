def fastatolist(file):
    seqList = []
    files=open(file, 'r')
    for lines in files:
        if lines[0] == ">":
            key = lines[1:]             
        else:
            seqList.append(lines.strip('\n'))
    return seqList

def measure_conservation(alignmentfile, output):
    seqList=fastatolist(alignmentfile)
    transpose=""
    transposedlist=[]
    for i in range(len(seqList[0])):
        for j in range(len(seqList)):
            transpose+=seqList[j][i]
        transposedlist.append(transpose)
        transpose=""
    
        
    totalcounter=0
    total_counts=[]
    commoncounter=0
    most_common_counts=[]
    for q in range(len(transposedlist)):
        for w in range(len(transposedlist[0])):
            if transposedlist[q][w]=="-":
                totalcounter+=1
        total_counts.append(totalcounter)
        totalcounter=0
    

    outputfile=open(output, "w")


    for t in range(0, 279):
        outputfile.write(str(t+1)+"\t"+ str(total_counts[t])+"\n")

    return outputfile

out= measure_conservation("TPD52-aligned.fas", "numOfGaps.txt")