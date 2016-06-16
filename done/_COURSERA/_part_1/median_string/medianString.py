import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_1')))

import hammingDistance as hD
import numberToPattern as nTp

def medianString(Dna, k):
	distance = float('inf')
	for i in xrange(0,pow(4,k)):
		Pattern = nTp.numberToPattern(i, k)
		distance_ = distanceBetweenPatternAndString(Pattern, Dna)
		if distance > distance_:
			distance = distance_
			Median = Pattern
	return Median

def medianStrings(Dna, k):
	distance = float('inf')
	for i in xrange(0,pow(4,k)):
		Pattern = nTp.numberToPattern(i, k)
		distance_ = distanceBetweenPatternAndString(Pattern, Dna)
		if distance > distance_:
			distance = distance_
			Median = [Pattern]
		if distance == distance_:
			Median.append(Pattern)
	return Median

def distanceBetweenPatternAndString(Pattern, Dna):
	k = len(Pattern)
	distance = 0
	for Text in Dna:
		hammingDistance = float('inf')
		for Pattern_ in hD.textToPatternsList(Text, k):
			hammingDistance_ = hD.hammingDistance(Pattern_, Pattern)
			if hammingDistance > hammingDistance_:
				hammingDistance = hammingDistance_
		distance += hammingDistance
	return distance

#print medianStrings(["CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC", "GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC", "GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"], 7)