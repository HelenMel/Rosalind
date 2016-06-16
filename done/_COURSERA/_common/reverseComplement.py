complementItems = { 'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

def reverseComplement(Pattern):
	return reverse_complement(Pattern)

def reverse_complement(Pattern):
	def compement(x):
		return complementItems[x]
	return "".join(map(compement, Pattern))[::-1]