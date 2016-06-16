import sys, os
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_1')))

import nucleotides as info
import hammingDistance as hD

def score(Motifs):
	Profile = profileFromMotifs(Motifs)
	return scoreForMotifsAndProfile(Motifs, Profile)

def scoreForMotifsAndProfile(Motifs, Profile):
	mostPopular = mostPopularWithProfile(Profile)
	return sum([hD.hammingDistance(m, mostPopular) for m in Motifs])

def profileFromMotifs(Motifs):
	t = len(Motifs)
	Counts = countsFromMotifs(Motifs)
	Profile = profileFromCounts(Counts, t)
	return Profile

def profileFromMotifsWithPseudo(Motifs):
	t = len(Motifs)
	Counts = countsFromMotifs(Motifs)
	Counts, t = addOneToEveryCount(Counts, t)
	Profile = profileFromCounts(Counts, t)
	return Profile

def countsFromMotifs(Motifs):
	m = len(Motifs[0])
	t = len(Motifs)
	Counts = [[0 for col in xrange(0, m)] for row in xrange(0, 4)]
	for Motif in Motifs:
		addValueToItemsFromMotif(Counts, Motif, 1)
	return Counts

def profileFromCounts(Counts, t):
	def toMedian(x, t):
		return float(x) / t
	return [[toMedian(x, t) for x in y] for y in Counts]

def addOneToEveryCount(exCounts, t):
	def addOne(x):
		return x + 1
	Counts = [[addOne(x) for x in y] for y in exCounts]
	t += len(exCounts)
	return (Counts, t)

def addValueToItemsFromMotif(Items, Motif, value):
	clumps = map(info.letterToNumber, list(Motif))
	for i in xrange(0, len(clumps)):
		Items[clumps[i]][i] += value
	return Items

def mostPopularWithProfile(Profile):
	p = np.array(Profile)
	maxIndexes = np.argmax(p, axis = 0)
	return "".join(map(info.numberToLetter, maxIndexes))