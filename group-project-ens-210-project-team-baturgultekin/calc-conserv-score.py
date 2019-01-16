import re

def fastareader(filename):
	seqDict = {}
	with open(filename, "r") as f:
		icerik = f.read()
		myDict = [elem.replace("\n", "").strip("\r")  for elem in re.split(r'>.*\n', icerik) if elem != ""]

	keys = [item.lstrip(">") for item in icerik.split("\n") if item.startswith('>')]

	seqDict = dict(zip(keys, myDict))
	return seqDict


def consensusWithIdentity(sequences):
	consensus_sequence = ''
	consensus_vals = {}
	for index, amino_acid in enumerate(sequences[0]):
		counter = {}
		for sequence in sequences:
			if index < len(sequence):
				if sequence[index] in counter.keys():
					counter[sequence[index]] += 1
				else:
					if sequence[index] != "-":
	 					counter[sequence[index]] = 1
		maxOne = max(counter, key=counter.get)
		#print(maxOne)

		if counter[maxOne] == 0:
			consensus_sequence += '-'
			consensus_vals[index] = 0			
		else:
			consensus_sequence += maxOne
		#	print counter[maxOne] , sum(counter.values())
			consensus_vals[index] = round(float(counter[maxOne])/sum(counter.values()), 8)
		#	print (consensus_vals)
	return consensus_sequence , consensus_vals


def main():
	myDict = fastareader("./yeniVeriler/ENOG4111M9H-aligned.fas")
	consensus_seq, consensus_vals = consensusWithIdentity(list(myDict.values()))

	with open("./yeniVeriler/identity.txt", "w") as f:
		f.write("Pos\tAA\tCons_Grad\n")
		for key in consensus_vals.keys():
			f.write("{}\t{}\t{}\n".format(key+1, consensus_seq[key], consensus_vals[key]))

	print("[*] Done")


if __name__ == "__main__":
	main()
