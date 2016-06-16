import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import spectralConvolutionProblem as sCP
import leaderboardCyclopeptideSequencing as lCS

def convolutionCyclopeptideSequencing(M, N, Spectrum):
	massSet = selectMostFrequentItems(sCP.convolution(Spectrum), M)
	#print "best items", massSet
	return lCS.leaderboardCyclopeptideSequencingWithMass(Spectrum, N, massSet)

def selectMostFrequentItems(Items, M):
	filterItems = [x for x in Items if (x < 201 and x > 56)]
	sortedItems =  sorted([(Items.count(e), e) for e in set(filterItems)], reverse = True)
	bestItems = sortedItems
	for j in xrange(M, len(Items)):
		if sortedItems[j][0] < sortedItems[M - 1][0]:
			bestItems = sortedItems[:j]
			break
	return [x[1] for x in bestItems]

print selectMostFrequentItems(sCP.convolution([0, 57, 118, 179, 236, 240, 301]), 1)
#print convolutionCyclopeptideSequencing(20, 60, [57, 57, 71, 99, 129, 137, 170, 186, 194, 208, 228, 265, 285, 299, 307, 323, 356, 364, 394, 422, 493])