import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_1')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import hammingDistance as hd
import numberToPattern as nTp

nucleotides = ['A', 'C', 'G', 'T']

def closeNeighbors(Text, k, d):
	patternsCount = pow(4,k)
	Close = [0] * patternsCount
	for i in xrange(0, len(Text) - k + 1):
		Neighborhood = neighbors(Text[i : i + k], d)
		for Pattern in Neighborhood:
			index =  nTp.patternToNumber(Pattern)
			Close[index] = 1
	return Close

def closeNeighborsLines(Text, k, d):
	fArray = closeNeighbors(Text, k, d)
	indexes = [i for i, x in enumerate(fArray) if x != 0]
	return set([nTp.numberToPattern(x, k) for x in indexes])

def neighbors(Pattern, d):
	if d == 0:
		return [Pattern]
	if len(Pattern) == 1:
		return nucleotides
	Neighborhood = set()
	suffix = Pattern[1:]
	first = Pattern[0]
	suffixNeighbors = neighbors(suffix, d)
	for Text in suffixNeighbors:
		if hd.hamming_distance(suffix, Text) < d:
			for symbol in nucleotides:
				Neighborhood.add(symbol + Text)
		else:
			Neighborhood.add(first + Text)
	return Neighborhood

