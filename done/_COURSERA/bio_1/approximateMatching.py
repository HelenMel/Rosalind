import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_1')))

import hammingDistance

def approximate_matching(Pattern, Genome, maxDistance):
	approximatePatternsIdx = []
	pL = len(Pattern)
	for index in xrange(0, len(Genome) - pL + 1):
		cPattern = Genome[index: index + pL]
		dist = hammingDistance.hamming_distance(Pattern, cPattern)
		if hammingDistance.hamming_distance(Pattern, cPattern) <= maxDistance:
			approximatePatternsIdx.append(index)
	return approximatePatternsIdx

def approximate_count(Pattern, Genome, maxDistance):
	count = 0
	pL = len(Pattern)
	for index in xrange(0, len(Genome) - pL + 1):
		cPattern = Genome[index: index + pL]
		if hammingDistance.hamming_distance(Pattern, cPattern) <= maxDistance:
			count += 1
	return count