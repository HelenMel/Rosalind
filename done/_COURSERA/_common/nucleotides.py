import readFile

nucleotides = ['A', 'C', 'G', 'T']
ribonucleotides = ['A', 'C', 'G', 'U']
acidsCount = 20

def letterToNumber(letter):
	return nucleotides.index(letter)

def numberToLetter(number):
	return nucleotides[number]

def codonTable():
	lines = readFile.listFromFile('../_common/RNA_codon_table.txt')
	table = dict([line.split(" ") for line in lines])
	return table

def massIntTable():
	lines = readFile.listFromFile('../_common/integer_mass_table.txt')
	def massItem(line):
		key, massS = line.split(" ")
		return (key, int(massS))
	table = dict([massItem(line) for line in lines])
	return table

def massIntSet():
	lines = readFile.listFromFile('../_common/integer_mass_table.txt')
	def massItem(line):
		key, massS = line.split(" ")
		return int(massS)
	return set([massItem(line) for line in lines])

#print massIntSet()