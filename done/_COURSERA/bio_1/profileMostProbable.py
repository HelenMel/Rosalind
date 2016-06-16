import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_1')))

import nucleotides as info
import hammingDistance as hD

def profileMostProbable(Text, k, Profile):
	probability = 0
	MostProbable = Text[:k]
	for Pattern in hD.textToPatternsList(Text, k):
		probability_ =  patternProbability(Pattern, Profile)
		if probability < probability_:
			MostProbable = Pattern
			probability = probability_
	return MostProbable

def patternProbability(Pattern, Profile):
	probability = 1
	for i in xrange(0, len(Pattern)):
		nucleotide = Pattern[i]
		j = info.nucleotides.index(nucleotide)
		profileValue = Profile[j][i]
		if profileValue == 0:
			return 0
		probability *= profileValue
	return probability


