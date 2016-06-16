import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_1')))

import closeNeighbors as cN

def motifEnumeration(Dna, k, d):
	Patterns = set()
	Samples = []
	for pattern in Dna:
		Samples.append(cN.closeNeighborsLines(pattern, k, d))
	resultSet = Samples[0]
	for patternSet in Samples:
		resultSet = resultSet & patternSet
	return resultSet


def stringToPatternsList(string, k):
	return [string[x: x+k] for x in xrange(0, (len(string) - k + 1))]