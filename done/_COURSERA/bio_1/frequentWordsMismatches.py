import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_1')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import hammingDistance as hd
import numberToPattern as nTp
import approximateMatching as aM
import reverseComplement as rC
import closeNeighbors as cN

def frequent_words_and_reverse_with_mismatches(Text, k, d):
	close = closeNeighbors(Text, k, d)
	fArray = frequencyArrayAndReverse(close, Text, k, d)
	return maxPatterns(fArray, k)

def frequencyArrayAndReverse(Close, Text, k, d):
	patternsCount = pow(4,k)
	fArray = [0] * patternsCount
	for i in xrange(0, patternsCount):
		if Close[i] == 1:
			if fArray[i] > 0:
				continue
			Pattern = nTp.numberToPattern(i, k)
			ReversePattern = rC.reverse_complement(Pattern)
			anotherIndex = nTp.patternToNumber(ReversePattern)
			totalSum = aM.approximate_count(Pattern, Text, d) + aM.approximate_count(ReversePattern, Text, d)
			fArray[i] = totalSum
			fArray[anotherIndex] = totalSum
	return fArray

def frequent_words_with_mismatches(Text, k, d):
	close = closeNeighbors(Text, k, d)
	fArray = frequencyArray(close, Text, k, d)
	return maxPatterns(fArray, k)

def maxPatterns(fArray, k):
	maxCount = max(fArray)
	indexes = [i for i, x in enumerate(fArray) if x == maxCount]
	return set([nTp.numberToPattern(x, k) for x in indexes])

def frequencyArray(Close, Text, k, d):
	patternsCount = pow(4,k)
	fArray = [0] * patternsCount
	for i in xrange(0, patternsCount):
		if Close[i] == 1:
			Pattern = nTp.numberToPattern(i, k)
			fArray[i] = aM.approximate_count(Pattern, Text, d)
	return fArray

def closeNeighbors(Text, k, d):
	return cN.closeNeighbors(Text, k, d)

def neighbors(Pattern, d):
	return cN.neighbors(Pattern, d)