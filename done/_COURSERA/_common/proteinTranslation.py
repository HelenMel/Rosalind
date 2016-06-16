import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import nucleotides as info

def rnaToProtein(Rna):
	# codon length
	k = 3
	codonTable = info.codonTable()
	def lineToProtein(line, i, k):
		codon = line[i: i + k]
		return codonTable[codon]
	proteins = [lineToProtein(Rna, i, k) for i in xrange(0, len(Rna), k)]
	return "".join(proteins)

#print rnaToProtein("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")