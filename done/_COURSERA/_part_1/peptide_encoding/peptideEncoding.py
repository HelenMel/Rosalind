import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import nucleotides as info
import proteinTranslation as pT
import reverseComplement as rC

def peptideEncoding(Dna, Peptide):
	Patterns = allDnaPatterns(Dna)
	parts = [patternToParts(pattern, len(Peptide)) for pattern in Patterns]
	#print parts

	def filterPeptide(part, Peptide):
		reversePart = rC.reverseComplement(part)
		return isDnaStringPeptide(x, Peptide) or isDnaStringPeptide(reversePart, Peptide)

	possibleEncodings = [[x for x in y if filterPeptide(x, Peptide)] for y in parts]
	#print possibleEncodings
	def reduceArray(x, y):
		return x + y
	return reduce(reduceArray, possibleEncodings)

def patternToParts(Pattern, codedLen):
	# step is equal to decoded lenght
	patternLen = codedLen * 3
	step = 3
	parts = [Pattern[i: i + patternLen] for i in xrange(0, len(Pattern), step)]
	return parts
	
def allDnaPatterns(Dna):
	Patterns = [ Dna ]
	Patterns.append(Dna[1:])
	Patterns.append(Dna[2:])
	return Patterns

def dnaToRna(Dna):
	def replacement(letter):
		index = info.letterToNumber(letter)
		return info.ribonucleotides[index]
	return "".join([replacement(x) for x in list(Dna)])

def isDnaStringPeptide(Dna, Peptide):
	rnaPart = dnaToRna(Dna)
	return isRnaStringPeptide(rnaPart, Peptide)

def isRnaStringPeptide(Rna, Peptide):
	if len(Rna) < (len(Peptide) * 3):
		return False
	return pT.rnaToProtein(Rna) == Peptide

#print peptideEncoding("ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA", "MA")