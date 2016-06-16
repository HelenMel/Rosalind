import sys, os
import random
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_1')))

import motifScore as mS
import profileMostProbable as pMP

def repeatedRandomMotifSearch(Dna, k, t, N):
	BestMotifs = []
	bestMotifScore = sys.maxint
	for x in xrange(0, N):
		Motifs = randomMotifSearch(Dna, k, t)
		score = mS.score(Motifs)
		if score < bestMotifScore:
			BestMotifs = Motifs
			bestMotifScore = score
	return BestMotifs

def randomMotifSearch(Dna, k, t):
  	BestMotifs = [randomSubString(x, k) for x in Dna]
	bestMotifScore = mS.score(BestMotifs)
	while True:
		Profile = mS.profileFromMotifsWithPseudo(BestMotifs)
		Motifs = [pMP.profileMostProbable(line, k, Profile) for line in Dna]
		score = mS.score(Motifs)
		if score < bestMotifScore:
			BestMotifs = Motifs
			bestMotifScore = score
		else:
			return BestMotifs

def randomSubString(line, k):
	subStringStart = random.randint(0, (len(line) - k - 1))
	return line[subStringStart: subStringStart + k]
