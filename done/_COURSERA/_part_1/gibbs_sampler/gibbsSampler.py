import sys, os
import random
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_1')))

import motifScore as mS
import profileMostProbable as pMP
import hammingDistance as hD
import randomMotifSearch as rMS

def repeatedGibbsSampler(Dna, k, t, N, M):
	BestMotifs = []
	N = 100
	bestMotifScore = sys.maxint
	for x in xrange(0, M):
		Motifs = gibbsSampler(Dna, k, t, N)
		score = mS.score(Motifs)
		if score < bestMotifScore:
			BestMotifs = Motifs
			bestMotifScore = score
	print "best score", bestMotifScore
	return BestMotifs

def gibbsSampler(Dna, k, t, N):
	BestMotifs = rMS.repeatedRandomMotifSearch(Dna, k, t, 3)
	bestMotifScore = mS.score(BestMotifs)
	for x in xrange(1, N):
		i = random.randint(0, (t - 1))
		Motifs = copy.copy(BestMotifs)
		Motifs.pop(i)
		Profile = mS.profileFromMotifsWithPseudo(Motifs)
		Motif_i = randomMotifForProfileInText(Dna[i], k, Profile)
		Motifs.insert(i, Motif_i)
		score = mS.score(Motifs)
		if score < bestMotifScore:
			BestMotifs = Motifs
			bestMotifScore = score
	return BestMotifs

def randomMotifForProfileInText(Text, k, Profile):
	Probabilities = probabilitiesForTextAndProfile(Text, k, Profile)
	return randomMotifWithProbabilities(Probabilities, Text, k)

def probabilitiesForTextAndProfile(Text, k, Profile):
	Probabilities = [pMP.patternProbability(p, Profile) for p in hD.textToPatternsList(Text, k)]

	# my personal improvment
	def addSmall(x):
		if x < 0.001:
		return x + 0.001
	return [addSmall(x) for x in Probabilities]

def randomSubString(line, k):
	subStringStart = random.randint(0, (len(line) - k - 1))
	return line[subStringStart: subStringStart + k]

def randomMotifWithProbabilities(Probabilities, Text, k):
	randomIndex = randomIndexFromProbabilities(Probabilities)
	return Text[randomIndex : randomIndex + k]

def randomIndexFromProbabilities(Probabilities):
	ranges = probabilitiesRanges(Probabilities)
	randomIndex = random.random()
	return firstIndexOfBiggerItem(ranges, randomIndex)

# def weighted_choice(choices):
#    total = sum(w for c, w in choices)
#    r = random.uniform(0, total)
#    upto = 0
#    for c, w in choices:
#       if upto + w >= r:
#          return c
#       upto += w
#    assert False, "Shouldn't get here"

def probabilitiesRanges(Probabilities):
	rangesSum = sum(Probabilities)
	#find
	ranges = []
	end = 0
	for x in xrange(0, len(Probabilities)):
		impact = Probabilities[x] / rangesSum
		newRange = (impact + end)
		end += impact
		ranges.append(newRange)
	return ranges

def firstIndexOfBiggerItem(Items, Number):
	index = 0
	while index < len(Items):
		if Items[index] > Number:
			return index
		index += 1
	return (len(Items) - 1)

#print weighted_choice([0.1, 0.2, 0.3])
#print randomIndexFromProbabilities([0.1, 0.2, 0.3])