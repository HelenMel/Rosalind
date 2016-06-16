import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_1')))

import profileMostProbable as pMP
import hammingDistance as hD
import nucleotides as info
import motifScore as mS

def greedyMotifSearch(Dna, k, t):
	return greedyMotifSearchWithFunction(Dna, k, t, makeProfileWithMotifAtStep)

def greedyMotifSearchPceudocounts(Dna, k, t):
	return greedyMotifSearchWithFunction(Dna, k, t, makeProfilePceudocounts)

def greedyMotifSearchWithFunction(Dna, k, t, makeProfile):
	Motifs = [hD.textToPatternsList(text,k) for text in Dna]
	BestMotifs = [Motifs[i][0] for i in xrange(0, t)]
	bestMotifScore = mS.score(BestMotifs)
	for Motif in Motifs[0]:
		Motifs_ = [ Motif ]
		Profile = None
		for i in xrange(1, t):
			Profile = makeProfile(Profile, Motifs_, i - 1)
			MostProbable = pMP.profileMostProbable(Dna[i], k, Profile)
			Motifs_.append(MostProbable)
		score = mS.score(Motifs_)
		if score < bestMotifScore:
			bestMotifScore = score
			BestMotifs = Motifs_
	return BestMotifs
			
def makeProfileWithMotifAtStep(exProfile, Motifs, step):
	if exProfile is None:
		Profile = initialProfileForMotif(Motifs[step])
	else:
		Profile = updateProfileWithPattern(exProfile, Motifs[step], step)
	return Profile
	
def makeProfilePceudocounts(exProfile, Motifs, step):
	return mS.profileFromMotifsWithPseudo(Motifs)

def initialProfileForMotif(Motif):
	Profile = [[0 for col in xrange(0, len(Motif))] for row in xrange(0, 4)]
	mS.addValueToItemsFromMotif(Profile, Motif, 1.0)
	return Profile

def updateProfileWithPattern(Profile, Motif, n):
	scale = float(n) / (n + 1)
	one = float(1) / (n + 1)
	def updateItemScale(item, scale):
		return item * scale
	Profile = [[updateItemScale(i, scale) for i in x] for x in Profile]
	mS.addValueToItemsFromMotif(Profile, Motif, one)
	return Profile

#print makeProfilePceudocounts(None, ["ACCT", "ATGT"], 1)