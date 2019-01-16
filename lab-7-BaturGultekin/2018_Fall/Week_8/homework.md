# ENS210: Computational Biology - Fall 2018 - Homework #1

## Homework `(10 pts)` 
**Due Nov 22nd 2018 12:00pm**

Write a python function to evaluate a multiple sequence alignment (for DNA) using the "sum of pairs" algorithm. The function should take 4 inputs: (i) MSA file in FASTA format; (ii) Match score; (iii) Mismatch score; (iv) Gap penalty.

(8 pts)

Write a code that runs the sum of pairs function in two DNA sequence alignments that you generated in lab 7: `DNA_alignment_1.fas` and `DNA_alignment_2.fas`. Use +1 for match -1 for mismatch and -2 for gap. Remember that gap-gap match should be ignored (value 0). 

Based on the parameters we define, which MSA is the better one? Write your answer here. (2pts)

```

```

The below is a hint. It might only be a part of your script. You are free to use it, but you don't have to.

```
people = ["Lisa","Pam","Maurice","Richard","John","Graham"]

def getpairs(source):
        result = []
        for p1 in range(len(source)):
                for p2 in range(p1+1,len(source)):
                        result.append([source[p1],source[p2]])
        return result

pairings = getpairs(people)
for pair in pairings:
        print(pair)
```

**Push your Python script.**

